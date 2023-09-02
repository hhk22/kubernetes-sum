
## Secret

configMap 에서는 비밀정보와 같은 값들은 그대로 노출되기 때문에 적절하지 않다.   
그런것들을 위해서 secret이 적절한 선택이 될 수 있다. 

아래와 같은 command로 생성할 수 있다. 

```
kubectl create secret generic mysql-cred \
  --from-literal=username='db-user' \
  --from-literal=password='hoon'
```

이렇게 되면 db-user, hoon과 같은 정보를 base64로 encoding해서 저장되고 이것을 yaml파일로 보면 알 수 있다. 

그것을 secret으로 선언하게 되면 아래와 같이 쓸 수 있다. 

```
apiVersion: v1
kind: Secret
metadata:
  name: mysql-cred
  namespace: default
data:
  username: ZGItdXNlcg==
  password: aG9vbg==
type: Opaque
```

이러한 secret정보는 여러 application에서 중요한 key로 엮어져있기 때문에, immutable 설정또한 가능하다. 

```
apiVersion: v1
kind: Secret
metadata:
  name: mysql-cred
  namespace: default
data:
  username: ZGItdXNlcg==
  password: aG9vbg==
type: Opaque
immutable: true
```

mysql과 위와 같은 secret정보를 사용하려면, env.valueFrom.secretKeyRef와 같은 정보로 사용하면 되고, 그것을 이용한 deployment는 아래와 같다. 

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    run: deploy-secretkeyref
  name: deploy-secretkeyref
spec:
  replicas: 1
  selector:
    matchLabels:
      app: deploy-secretkeyref
  template:
    metadata:
      labels:
        app: deploy-secretkeyref
    spec:
      containers:
      - image: sysnet4admin/mysql-auth 
        name: mysql-auth 
        env:
        # Need to init mysql 
        - name: MYSQL_ROOT_PASSWORD
          value: rootpassword
        # Custom auth 
        - name: MYSQL_USER_ID
          valueFrom:
            secretKeyRef:
              name: mysql-cred 
              key: username 
        - name: MYSQL_USER_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-cred 
              key: password 
        ports:
        - containerPort: 3306
        volumeMounts:
        - name: mysql-pvc
          mountPath: /var/lib/mysql
      volumes:
      - name: mysql-pvc
        persistentVolumeClaim:
          claimName: mysql-pvc
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pvc  
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 20Gi
  storageClassName: managed-nfs-storage 
```

그런데, 이러한 secret정보는 base64로 decoding하면 다시 알 수 있기때문에, secret에 대한 리소스를 rbac로 접근관리를 철저하게 하거나, 외부 서비스로 중요정보를 저장하는것이 좋은 대안이 될 수 있다. 

```
cat secret.yaml
>> ... data.username >> ZGItdXNlcg==

echo ZGItdXNlcg== | base64 --decode
>> db-user
```