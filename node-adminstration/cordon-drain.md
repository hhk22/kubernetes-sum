



```
# node의 scheduling을 disable 시키는 방법. 
kubectl cordon <node-name>

# node에 이미 scheduled 되어있는 pod들을 다른 node로 옮기는 바업ㅂ. 
kubectl drain w3-k8s --ignore-daemonsets --force 

# 해제. 
kubectl uncordon <node-name>

```