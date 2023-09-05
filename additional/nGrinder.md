

### nGrinder로 과부하를 일으켜서 HPA 사용해보기. 

- nGrinder의 구조는 kubernetes의 구조와 비슷하다.  
- controller가 존재한다. ( 감독관 같은 역할, 요청을 받으면 해당 요청을 agent들에게 알려주고, 해당 상황을 monitoring 한다. )
- agent들이 있고, 이것들이 nGrinder controller에 join하는 구조. 마치, kubernetes의 master/worker 의 구조. 
- agent들이 요청을 받으면 target server에 load를 주는 process. 


Controller 

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: ngrinder-controller
  name: ngrinder-controller
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ngrinder-controller
  template:
    metadata:
      labels:
        app: ngrinder-controller
    spec:
      containers:
      - name: ngrinder
        image: ngrinder/controller:3.5.4
        ports:
        # Controller's web port 
        - containerPort: 80
        # Health-chceck && Keepalive 
        - containerPort: 16001
        # Agents's ports 
        - containerPort: 12000
        ...
---
apiVersion: v1
kind: Service
metadata:
  name: ngrinder-controller-svc
spec:
  type: LoadBalancer
  selector:
    app: ngrinder-controller
  ports:
 # each of port has own purpose. See above 
  - name: port80
    port: 80
    targetPort: 80
  - name: port16001
    port: 16001
    targetPort: 16001
  - name: port12000
    port: 12000
    targetPort: 12000
 ...
```


80번 포트로 웹접속이 가능하고, controller와 agent는 12000번대 port로 통신한다. 
agent는 다음과 같이 작성. 

```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  labels:
    app: ngrinder-agent
  name: ngrinder-agent
spec:
  selector:
    matchLabels:
      app: ngrinder-agent
  template:
    metadata:
      labels:
        app: ngrinder-agent
    spec:
      containers:
      - name: ngrinder-agent
        image: ngrinder/agent:3.5.4
        args: [192.168.1.11:80]  # 위의 ngrinder lb service의 주소. 
```

이렇게 하고서, hpa와 연결된 deployment를 배포하게 되면, 
1. controller에서 agent에 load 요청을 주고
2. 각 node(DaemonSet)에서 load요청을 받고, 부하를 시작함. 
3. 부하가 되면, hpa에서 감지해, 임계치가 넘어가면 scale out을 시작함. 

이러한 구조로 동작한다. 