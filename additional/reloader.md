


## Reloader

ConfigMap이나 Secret과 같은 정보들을 바꾸게되더라도, 기존에 configMap, secret을 사용하고 있던 pod들은 적용되지 않는다. 
적용하려면, 다시 배포해야한다. 

그런데, Reloader ( https://github.com/stakater/Reloader )를 사용하게 되면, 변경된 configMap, secret에 따라서 재배포 된다. 


일단, reloader 배포. 


> kubectl apply -f https://raw.githubusercontent.com/stakater/Reloader/master/deployments/kubernetes/reloader.yaml


> k edit secrets mysql-cred


```
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    reloader.stakater.com/auto: "true" # for reloading secret  
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


여기서 ` reloader.stakater.com/auto: "true" # for reloading secret `  이 부분이 env와 연결된 configMap과 secret을 자동으로 연계해서 변경된 부분이 있으면 자동으로
rolling update를 해준다. 만약 조건을 변경하고 싶다면, github을 참조하면 된다. 

하지만, 이러한 configMap, secret 변경에 의한 deplotyment 자동 rolling update는 지양한다. 중요한 정보이기도 하고, 그래서 연계되어있는 부분도 많고, alpha, prod같은
운영서버에서는 이러한것들을 변경하는것이 정상적인 상황은 아니기 때문. 