

개념적으로는 sideCar, Ambassador, Adaptor 모두 존재하지만, 실제로는 sideCar를 주로 사용한다. 

- sideCar는 Pod에 포함되어 있는 Container 중 하나로, Pod의 주요 Container가 동작하는 동안 동작한다.
--> Container들은 각기 다른 역할을 수행하며, sideCar에서는 MainContainer가 있고, sideCarContainer가 있는 구조이다. 
--> ex) webServer container, logMonitor container

- Ambassador는 Pod의 주요 Container가 외부와 통신할 수 있도록 도와주는 Container이다.  
--> Proxy container를 생각하면 좋다. 
--> ex) application conatiner, Proxy Ambassador container
--> 이렇게되면, application은 그 기능 자체에만 집중할 수 있고, proxy는 네트워크 기능만 집중할 수 있다.

- Adaptor는 Pod의 주요 Container가 외부와 통신할 수 있도록 변환해주는 Container이다.
--> Adaptor는 연결된 pod의 출력을 통일 시켜준다. 
--> ex) Prometheus Adaptor
--> 이렇게 함으로써, 메인컨테이너는 다른 컨테이너와의 연결을 신경쓰지 않아도 된다.