
Helm 

```
helm repo add <repo_name> <repository URL>
helm repo update
helm search repo

helm install <image_name> <repo_name>/<repository_image> \
    --create-namespace \
    --namespace=... \
    --set ... \
    --set ... \
    -f ...

helm list -n <namespace>


```