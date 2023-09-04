


### kubectl 

kubectl만 설치되어있으면 어떤 곳에서도 kubernetes를 control 할 수 있다. 
kubectl이 kube-apiServer를 찾는 곳은 `/root/.kube/config` 이다. 
이곳에 관련한 정보를 넣어둔다면, apiServer에 원하는 요청을 할 수 있다.   

그래서 이러한, apiServer로의 접근을 철저히 제한을 걸어두어야 한다. 