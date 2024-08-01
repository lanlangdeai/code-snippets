# K8s

![img](https://cdn.nlark.com/yuque/0/2023/png/376699/1696562836677-350a6633-13e3-4586-80fe-776d69334b87.png)



【Master】

API server



Controller manager



Etcd



Scheduler

处理了 Pod 应该调度至哪个 Node





【Node】

### Kubelet

按照一般架构设计上的习惯，kubelet 所承担的角色一般会被叫做 agent，这里叫做 kubelet 很大程度上受 Borg 的命名影响，Borg 里面也有一个 Borglet 的组件存在。kubelet 便是 K8S 中的 agent，负责 Node 和 Pod 相关的管理任务。



作用：

1.首先便是要能够注册，让 server 端知道它的存在，所以这便是它的第一个作用：节点管理。

当我们执行 kubelet --help 的时候，会看到它所支持的可配置参数，其中有一个 --register-node 参数便是用于控制是否向 kube-apiserver 注册节点的，默认是开启的。

2.Pod管理，保障该 Pod 能按照预期，在对应 Node 上启动并保持工作

- 健康检查：通过 LivenessProbe 和 ReadinessProbe 探针进行检查，判断是否健康及是否已经准备好接受请求。
- 资源监控：通过 cAdvisor 进行资源监。

3.kubelet 的作用之一就是负责镜像拉取，而实际上，在镜像方面的错误主要预设了 6 种，分别是 ImagePullBackOff，ImageInspectError，ErrImagePull，ErrImageNeverPull，RegistryUnavailable，InvalidImageName。





### kube-proxy

我们都知道，想要访问某个服务，那要么通过域名，要么通过 IP。而每个 Pod 在创建后都会有一个虚拟 IP，K8S 中有一个抽象的概念，叫做 Service ，kube-proxy 便是提供一种代理的服务，让你可以通过 Service 访问到 Pod。



Container runtime

容器运行时最主要的功能是下载镜像和运行容器





------

Deployment

Deployment 是一种高级别的抽象，允许我们进行扩容，滚动更新及降级等操作



ReplicaSet

ReplicaSet 是一种较低级别的结构，允许进行扩容。

我们上面已经提到 Deployment 主要是声明一种预期的状态，并且会将 Pod 托管给 ReplicaSet，而 ReplicaSet 则会去检查当前的 Pod 数量及状态是否符合预期，并尽量满足这一预期。

ReplicaSet 可以由我们自行创建，但一般情况下不推荐这样去做，因为如果这样做了，那其实就相当于跳过了 Deployment 的部分，Deployment 所带来的功能或者特性我们便都使用不到了。

除了 ReplicaSet 外，我们还有一个选择名为 ReplicationController，这两者的主要区别更多的在选择器上，我们后面再做讨论。现在推荐的做法是 ReplicaSet



Service

Service 简单点说就是为了能有个稳定的入口访问我们的应用服务或者是一组 Pod。通过 Service 可以很方便的实现服务发现和负载均衡。



Service 目前有 4 种类型：

- ClusterIP： 是 K8S 当前默认的 Service 类型。将 service 暴露于一个仅集群内可访问的虚拟 IP 上。
- NodePort： 是通过在集群内所有 Node 上都绑定固定端口的方式将服务暴露出来，这样便可以通过 <NodeIP>:<NodePort> 访问服务了。
- LoadBalancer： 是通过 Cloud Provider 创建一个外部的负载均衡器，将服务暴露出来，并且会自动创建外部负载均衡器路由请求所需的 Nodeport 或 ClusterIP 。
- ExternalName： 是通过将服务由 DNS CNAME 的方式转发到指定的域名上将服务暴露出来，这需要 kube-dns 1.7 或更高版本支持。







问题排查：

1.describe

```
kubectl -n work describe pod/saythx-redis-7574c98f5d-v66fx
```



2.events

```
kubectl -n work get events
```
