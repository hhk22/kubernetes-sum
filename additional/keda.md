


### KEDA

HPA는 기존의 resource정보를 바탕으로 미리 설정해둔 임계치를 넘겼을때, scale-in, scale-out을 시행한다.  
각 node의 kubelet에는 cAdvisor라는 resource estimator가 존재하고, container runtime을 통해, cAdvisor가 수집한다.  
cAdvisor가 수집할 수 있는 정보는 metrics-server를 이용해 얻을 수 있다. ( 따로 설치해야함. )

- KEDA는 job, cronJob을 auto-scaling하는 scaledjobs, Deployment, statefulset, Custom Resource 를 auto-scaling하는 scaledobjects가 존재한다. 

- 해당 scaledObject가 배포되면, 그것을 참조하는 HPA가 배포되고, trigger의 조건이 만족되면, HPA를 통해 replicas를 변경하여 target object의 수를 조정하는 방식이다. 

- KEDA를 사용하는 이유는 trigger쪽에 다양한 scaler들을 제공한다. ( Prometheus, AWS, GCP, redis, ... )


```
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: keda-backend-scaledobject
spec:
  scaleTargetRef:
    name: keda-backend
  minReplicaCount: 1
  maxReplicaCount: 6
  pollingInterval: 5
  triggers:  
  - type: kubernetes-workload
    metadata:
      podSelector: 'app=keda-frontend'
      value: '3'
```

이렇게 되면, trigger 쪽에서, `app=keda-fronted` 인 pod의 갯수가 늘어나게 되면, `scaleTargetRef` 쪽에, `name:keda-backend` 가 3개 차이로 따라 올라가게된다. 
이처럼, trigger 에서 조건을 쓰고, scaleTargetRef 에 target을 사용하면 된다. 

기존의 hpa 만을 쓸때는, 기존의 resource 자원, cpu, memory와 같은 제한된 조건만을 trigger로 사용할 수 밖에 없었찌만, KEDA를 사용하게되면, 다양한 trigger를 사용할 수 있다. 
