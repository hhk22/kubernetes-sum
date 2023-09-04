
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

그러고서, metic server를 배포 ( https://github.com/kubernetes-sigs/metrics-server )
> kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

다음과 같은 순서로 hpa가 동작함. 

1. HPA 가 API서버에 정보를 요청
2. API 서버는 Metric-Server를 통해서 pod,node들에 대한 정보를 보냄. 
--> Metric server에 요청하면 Metric-server가 각 node들의 kubelet을 통해서 정보를 수집. 

그리고 해당 service로 curl를 계속 요청하면 cpu 부하가 올라가면서 pod의 갯수가 증가함. 