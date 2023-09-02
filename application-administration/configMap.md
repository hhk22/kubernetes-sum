
configMap.yaml

```
apiVersion: v1
kind: ConfigMap
metadata:
 name: sleepy-config 
data:
 STATUS: "WAKE UP"
 NOTE: "TestBed Configuration"
```

Deployment with ConfigMap

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: deploy-configmapref
  name: deploy-configmapref
spec:
  replicas: 1
  selector:
    matchLabels:
      app: deploy-configmapref
  template:
    metadata:
      labels:
        app: deploy-configmapref
    spec:
      containers:
      - image: sysnet4admin/sleepy 
        name: sleepy 
        command: ["/bin/sh","-c"]
        args:
        - |
          echo "sleepy $STATUS"
          echo "NOTE: $NOTE"
          sleep 3600
        envFrom:
        - configMapRef:
            name: sleepy-config
```

Deployment with ConfigMapKey

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: deploy-configmapkeyref
  name: deploy-configmapkeyref
spec:
  replicas: 1
  selector:
    matchLabels:
      app: deploy-configmapkeyref
  template:
    metadata:
      labels:
        app: deploy-configmapkeyref
    spec:
      containers:
      - image: sysnet4admin/sleepy 
        name: sleepy 
        command: ["/bin/sh","-c"]
        args:
        - |
          echo "sleepy $APP_STATUS"
          sleep 3600
        env:
        - name: APP_STATUS # mandantory field
          valueFrom:
            configMapKeyRef:
              name: sleepy-config
              key: STATUS
```

Deployment with ConfigMap Volume

> /etc/sleepy.d  
> cat /etc/sleepy.d/STATUS : WAKE UP
> cat /etc/sleepy.d/NODE : TestBed Configuration

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: deploy-vol-configMap
  name: deploy-vol-configmap
spec:
  replicas: 1
  selector:
    matchLabels:
      app: deploy-vol-configmap
  template:
    metadata:
      labels:
        app: deploy-vol-configmap
    spec:
      containers:
      - image: sysnet4admin/sleepy 
        name: sleepy 
        command: ["/bin/sh","-c"]
        args:
        - |
          sleep 3600
        volumeMounts:
        - name: appconfigvol
          mountPath: /etc/sleepy.d
      volumes:
      - name: appconfigvol
        configMap:
          name: sleepy-config
```


