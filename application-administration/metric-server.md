

각 node의 정보를 얻을 수 있는 metric-server

> https://github.com/kubernetes-sigs/metrics-server

MetricServerApi를 배포하게되면, 아래와 같은 가정을 거친다. 


1. kubectl top pod <pod_name>
2. kube-api-server가 metric-server로 request
3. metric-server가 각 node의 kubelet에 request
4. response to kube-api-server

