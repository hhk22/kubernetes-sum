
## LB Static IP

loadBalancer static IP 지정 가능. 

```

apiVersion: v1
kind: Service
metadata:
  name: lb-static-ip
spec:
  selector:
    app: static-ip
  ports:
    - name: http
      port: 80
      targetPort: 80
  type: LoadBalancer
  loadBalancerIP: 192.168.1.21

```

static IP 말고도, loadBalancer로 들어오는 IP range 또한 설정가능하다. 

```
apiVersion: v1
kind: Servcie
...
spec:
    ...
    type: LoadBalancer
    loadBalancerIP: 192.168.1.21
    loadBalancerSourceRanges:
    - 192.168.1.0/24

```

이렇게 하면, 192.168.1.0 - 192.168.1.255 의 source 만 loadBalancer에서 허용해준다.  

물론, RBAC, 인증과 관련한 설정들과 같은 방법들로 차단을 많이 하지만, 이와같이 kubernetes LB단에서도 허용IP를 지정해줄 수 있따. 