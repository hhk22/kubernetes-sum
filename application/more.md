

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

```
# Replicaset / ReplicationController
Replicaset: MatchedLabels / MatchedExpressions
ReplicationController : MatchedLabels, rolling-update

# RestartPolicy
restartPolicy: onFailure -> restart container
restartPolicy: Never -> restart pod (restarted by deployment)

# Service
- clusterIP < NodePort < LoadBalancer, 
- ExternalName

# topology
 


```

- 권한
    - kubectl 과 같은 명령어 --> user / group
        - certificate signing requests
    - pod와 같은 resource들이 권한 --> serviceaccount
- 네트워크
    - docker0 network (NAT)

- custom helm


