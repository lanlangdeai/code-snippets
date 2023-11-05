# Code-Snippets
代码片段

常用代码片段, 包括但不限于

+ 语言
  - PHP 
  - Python
  - Golang
  - Shell
  - Lua
  - NodeJS
  - Java
+ 数据库
  - MySQL
  - PostgreSQL
  - ClickHouse
+ 缓存
  - Redis
  - MongoDB
  - ElasticSearch
+ 注册发现
  - Consul
  - Etcd
+ 配置中心
  - Apollo
  - Nacos
+ Web软件
  - Nginx
  - Apache
+ 容器化
  - [Docker](docker/Docker.md)
  - K8s
+ 操作系统
  - Linux
  - Centos
  - Ubuntu





---

### PHP

#### 环境搭建

本地开发

- Xampp(window+mac)
https://www.apachefriends.org/

- PhpStudy
https://www.xp.cn/

- ServBay(Mac)
https://www.servbay.dev/zh_CN

- xdebug: 代码调试/debug
https://github.com/xdebug/xdebug



#### Web框架
- laravel-s: 介于laravel/lumen与swoole的适配器
https://github.com/hhxsv5/laravel-s
- dingo/api: 基于laravel/lumen框架的restful api包
https://github.com/dingo/api


- yii2-sentry: 适用于Yii2框架的sentry包
https://github.com/notamedia/yii2-sentry


- Hpyerf: 使用docker部署开发环境
https://github.com/hyperf/hyperf-docker








#### 第三方类库
- laravel-uuid: 生成uuid
https://github.com/webpatser/laravel-uuid

- sso: SSo实现包
https://github.com/evangui/sso


- oauth2: OAUTH2.0实现
https://github.com/thephpleague/oauth2-client

- OpenID: OpenId连接授权
https://github.com/jumbojett/OpenID-Connect-PHP


#### 相关工具
- 项目发布工具
https://github.com/REBELinBLUE/deployer




- Composer镜像源切换工具
https://github.com/slince/composer-registry-manager




### Python

#### 第三个类库

- psutil: 查看系统信息(内存,CPU等)
https://github.com/giampaolo/psutil



#### 面试资源

- https://github.com/kenwoodjw/python_interview_question




---


### Golang

#### 第三方库
- protoc-go-inject-tag: proto文件,tag注入
https://github.com/favadi/protoc-go-inject-tag

- g: golang版本管理工具
https://github.com/voidint/g

- Asynq: 异步任务处理
https://github.com/hibiken/asynq

- asynqon: Asynq异步任务处理的Web UI工具(类Celery的Flower)
https://github.com/hibiken/asynqmon

- redigo: Redis客户端包1
https://github.com/gomodule/redigo
- go-redis: Redis客户端包2
https://github.com/redis/go-redis

- mongo-go-driver: MongoDB客户端
https://github.com/mongodb/mongo-go-driver

- nsq: 分布式消息平台
https://github.com/nsqio/nsq


- cobra: Cli应用程序库(类Python中的Click)
https://github.com/spf13/cobra

- pflag: 程序参数处理(类Python中的argparse) 
https://github.com/spf13/pflag

- shopspring/decimal: 浮点数精度处理
https://github.com/shopspring/decimal

- copier: 结构体复制
https://github.com/jinzhu/copier


- 从一个类型转换为另一种类型
https://github.com/spf13/cast

- go-spew: 友好的打印
https://github.com/davecgh/go-spew

- golang-set: 集合
https://github.com/deckarep/golang-set



- shima-park/agollo: 携程Apollo Golang版客户端
https://github.com/shima-park/agollo

- Kafka 客户端1
https://github.com/twmb/franz-go
- Kafka 客户端2
https://github.com/confluentinc/confluent-kafka-go
- Kafka 客户端3(*)
https://github.com/IBM/sarama


- guuid: 生成uuid1
https://github.com/nu7hatch/gouuid
- uuid: 生成uuid2
https://github.com/google/uuid
- go.uuid: 生成uuid3
https://github.com/satori/go.uuid

- shortid: 短小ID生成
https://github.com/teris-io/shortid


- satori/go.uuid: 分布式ID(雪花)
https://github.com/satori/go.uuid
- snowflake: 雪花分片
https://github.com/bwmarrin/snowflake


- bigcache: 高效的内存缓存库
https://github.com/allegro/bigcache
- go-cache: 高效的内存缓存库
https://github.com/patrickmn/go-cache


- json-iterator/go: 高效的JSON序列化工具
  https://github.com/json-iterator/go

- sonic: 一个速度奇快的 JSON 序列化/反序列化库
https://github.com/bytedance/sonic


- gjon: json数据解析
https://github.com/tidwall/gjson


- prometheus/client_golang: prometheus的golang语言客户端包
https://github.com/prometheus/client_golang



- gin-contrib/pprof: gin框架的pprof中间件
https://github.com/gin-contrib/pprof

- gin-swagger: gin框架生成swagger文档中间件
https://github.com/swaggo/gin-swagger

- wire: 依赖注入工具
https://github.com/google/wire



- juju/ratelimit: 限流
https://github.com/juju/ratelimit

- uber-go/ratelimit: 限流
https://github.com/uber-go/ratelimit

- mux: http 路由包
https://github.com/gorilla/mux


- gout 是go写的http 客户端，为提高工作效率而开发
https://github.com/guonaihong/gout

- cron: 定时任务
https://github.com/robfig/cron

- 日志分割
https://github.com/natefinch/lumberjack


- zap: 日志管理工具1
https://github.com/uber-go/zap
- logrus: 日志管理工具2
https://github.com/sirupsen/logrus
- zerolog: 日志管理工具3
https://github.com/rs/zerolog

- converter: mysql表结构自动生成golang struct
https://github.com/gohouse/converter

- gorequest: 发起http网络请求
https://github.com/parnurzeal/gorequest
- resty: 发起http网络请求
https://github.com/go-resty/resty


- viper: 配置管理
https://github.com/spf13/viper

- cleanenv: 纯净配置管理工具
https://github.com/ilyakaznacheev/cleanenv

- gopsutil: 查看系统信息(内存,CPU)
https://github.com/shirou/gopsutil


- 生成二维码
https://github.com/skip2/go-qrcode

- 探测媒体,文件的类型
https://github.com/gabriel-vasile/mimetype


- wecom-go-sdk: 企业微信应用接入
https://github.com/go-laoji/wecom-go-sdk

#### Web框架

- Echo
https://github.com/labstack/echo
https://echo.labstack.com/




#### 微服务
- go-kit
https://github.com/go-kit/kit


- hertz: 字节推出的微服务框架
https://github.com/cloudwego/hertz

- kratos: 哔哩哔哩推出的微服务框架
https://github.com/go-kratos/kratos



#### Github
Golang学习
  - https://github.com/jiujuan/go-collection
  - https://github.com/sdgmf/go-project-sample
  - https://github.com/jincheng9/go-tutorial
  - https://github.com/golang/example


进阶学习
  - https://github.com/xinliangnote/go-gin-api
  - 



代理池搭建
  - https://github.com/henson/proxypool

博客平台搭建
  - https://github.com/go-sonic/sonic




代码风格
- https://github.com/uber-go/guide
Go项目结构
- https://github.com/golang-standards/project-layout
- https://github.com/evrone/go-clean-template




代码检测工具
- https://github.com/golangci/golangci-lint
Go-Build模版
- https://github.com/thockin/go-build-template



#### 面试
- https://github.com/lifei6671/interview-go



### Rust

- 学习教程
https://github.com/sunface/rust-by-practice



---



### Redis

- 布隆过滤器模块
https://github.com/RedisBloom/RedisBloom




### K8s


- Krew:  kubectl 插件的包管理器。
https://github.com/kubernetes-sigs/krew


- kubectx: 在kubectl中在集群和名称空间之间切换的工具
https://github.com/ahmetb/kubectx

- minikube: 适用于本地搭建k8s单机服务的工具
https://github.com/kubernetes/minikube

- rancher: 搭建生产环境k8s集群工具
https://github.com/rancher/rancher

- rancher-desktop
https://github.com/rancher-sandbox/rancher-desktop


- 基于docker-desktop搭建的k8s环境
https://github.com/AliyunContainerService/k8s-for-docker-desktop

#### 学习教程
Github:
- https://github.com/guangzhengli/k8s-tutorials
- https://github.com/dockersamples/example-voting-app



### DevOps

- bytebase: devpos 平台
https://github.com/bytebase/bytebase


#### 学习教程
- https://github.com/bregman-arie/devops-exercises

Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoSQL, Azure, GCP, DNS, Elastic, Network, Virtualization. DevOps Interview


---


### Linux

- linux的终端可视化工具
https://github.com/sqshq/sampler


- Upx: 文件压缩工具
https://github.com/upx/upx




---



### Js+Css


- 字体图标
https://github.com/ryanoasis/nerd-fonts



#### 工具

- json文件查看与管理工具
https://github.com/triggerdotdev/jsonhero-web





### 机器学习

- https://github.com/microsoft/ML-For-Beginners



## 编辑器
IDE使用教程(PHPstorm,Pycharm,Goland,WebStorm,DataGrip等)
- https://github.com/judasn/IntelliJ-IDEA-Tutorial



## 周边服务
[IP]
1. https://www.ipip.net




## 使用软件&工具
- typora-activation: Typora激活工具
https://github.com/markyin0707/typora-activation

  
- Etcd的可视化客户端
https://github.com/gtamas/etcdmanager

- Zookeeper GUI工具
https://github.com/vran-dev/PrettyZoo

- uPic: 图片上传工具(Mac)
https://github.com/gee1k/uPic
- Cloudreve: 云盘系统
https://github.com/cloudreve/Cloudreve

- 代码片段管理软件
https://github.com/massCodeIO/massCode



- wrk: 性能测试工具
https://github.com/wg/wrk



## 平台类
- 静态导航网站
https://github.com/WebStackPage/WebStackPage.github.io

- 站点监控工具(Uptime)
https://github.com/louislam/uptime-kuma


## 公共资源列表
- Etcd: https://github.com/etcd-io/etcd
- Apollo: https://github.com/apolloconfig/apollo-quick-start
- Proto Buffer: https://github.com/protocolbuffers/protobuf
- 



## 码如人生
- 程序员的副业: https://github.com/easychen/lean-side-bussiness
- 



