
여러개의 manifest 관리를 위한 편리한 도구 Kustomize


```
kubectomize create --autodetect

// 이렇게 하면 아래와 같은 형태로 kubetomization.yaml을 생성
resources:
    - deployment.yaml
    - service.yaml
    ...
```

자동으로 image를 변경하고 그에 대한 manifest를 자동으로 생성해줌.

```
kustomize edit set image nginx:latest

kustomize build
kustomize build | kubectl apply -f -
kubectl describe pods -n metallb-system | grep Image:
```

