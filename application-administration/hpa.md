
각 pod의 cpu request,limit을 타이트하게 주고, curl명령어를 계속 날려서 부하를 주게해서 HPA를 이용해보자. 

아래와 같은 명령어를 사용해도 되고, 

> k autoscale deployment deploy-4-hpa --min=1 --max=10 --cpu-percent=50

아래와 같은 yaml파일을 써도 됨. 

```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: deploy-4-hpa
spec:
  maxReplicas: 10
  minReplicas: 1
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: deploy-4-hpa
  targetCPUUtilizationPercentage: 50
```
이렇게 하면 hpa 리소스가 배포됨. 
그리고 hpa가 바라보는 resource를 배포. 

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-4-hpa
  labels:
    app: deploy-4-hpa
spec:
  replicas: 1
  selector:
    matchLabels:
      app: deploy-4-hpa
  template:
    metadata:
      labels:
        app: deploy-4-hpa
    spec:
      containers:
      - name: chk-hn
        image: sysnet4admin/chk-hn
        resources:
          requests:
            cpu: "10m"
          limits:
            cpu: "20m"
---
apiVersion: v1
kind: Service
metadata:
  name: lb-deploy-4-hpa 
spec:
  selector:
    app: deploy-4-hpa
  ports:
    - name: http
      port: 80
      targetPort: 80 
  type: LoadBalancer
```

그리고 해당 service로 curl를 계속 요청하면 cpu 부하가 올라가면서 pod의 갯수가 증가함. 