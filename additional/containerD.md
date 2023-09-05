

### containerD vs DockerShim


기존의 Kubernetes과 Docker 사이에서는 Kubernetes에서 표준화 된 API 인 CRI (Container Runtime Interface) 에 의해 교환이 이루어집니다.  
그러나 Docker는 현재 CRI를 기본적으로는 지원하지 않기 때문에 Kubernets과 Docker는 `dockershim` 라는 다리를 통해 교환이 이루어지고 있습니다.

그 이후, docker 의 런타임이 containerD로 변경되면서, kubelet과 호환되기 위해서는 새로운 interface가 필요했고, 그것이 `Cri-containerd` 입니다. 
그러나, 이런 interface가 daemon으로 떠있을 필요없이, 새로운 containerD에서는 `Cri-containerd`를 plugin 형식으로 지원하게 되면서 (내장되어있음),
간편하고 빨라졌습니다. 더이상 불필요한 daemon이 필요가 없게된거라고 볼 수 있다. 

