
기존의 배포서비스는 deployment에서 replicaset을 이용해서 pod를 교체한다. 

1. pod교체 요청
2. 새로운 replicaset을 생성 ( 기존 replicaset 존재 )
3. 기존,새로운 replicaset의 desired를 조정하면서 교체
4. 기존 replicaset.desired : 0 // new replicaset.desired : n


일단, 기존의 이미지를 배포하고, rollout은 아래와 같은 과정을 거친다. 

```
kubectl set image deployment deploy-rollout nginx=nginx:1.21.0

kubectl rollout status deployment deploy-rollout
kubectl rollout history deployment deploy-rollot

// undo
kubectl rollout undo deployment deploy-rollout

```