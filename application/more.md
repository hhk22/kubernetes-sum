

```
# multi container  
kubectl exec multi-pod -c nginx-container -it -- /bin/bash -p 80

> 동일 파드에 있는 container들은 동일 IP를 가지고 있음

```

```

# Init conatiner 조구조

init container: DB
main container: application using DB

```

```
# Pause conatiner
pod마다 하나씩 만들어짐.
pod의 인프라를 구성해주는 container

--> Pause container 확인하는 방법.
ssh docker-container

```


- Replicaset / ReplicationController
    - MatchedExpressions
- Replicaset / Deployment
    - Rolling Update 순서
    - Daemonset은 그냥 kubectl edit으로도 rolling update가 되는데. deployment도 된다. 
    그렇다면 rollingupdate와 edit의 차이점은? 
- job restart policy: onFailure -> container재시작
- job restart policy: Never -> pod재시작
- ExternalName, LB > NodePort > clusterIP
- headless coreDNS pod endpoint 설정해줌. 
- Canary 배포 전략
- topology 다시 공부

