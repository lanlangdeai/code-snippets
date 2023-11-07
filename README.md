# Code-Snippets
代码片段

常用代码片段, 包括但不限于

+ 语言
  - [PHP](php/PHP.md)
  - [Python](python/Python.md)
  - [Golang](golang/Go.md)
  - [Shell](shell/Shell.md)
  - [Lua](lua/Lua.md)
  - [NodeJS](nodejs/NodeJS.md)
  - [Java](java/Java.md)
+ 数据库
  - [MySQL](mysql/MySQL.md)
  - [PostgreSQL](postgreSQL/PostgreSQL.md)
  - [ClickHouse](clickhouse/Clickhouse.md)
+ 缓存
  - [Redis](redis/Redis.md)
+ 文档型
  - [MongoDB](mongodb/MongoDB.md)
  - [ElasticSearch](elasticSearch/ElasticSearch.md)
+ 注册发现
  - [Consul](consul/Consul.md)
  - [Etcd](etcd/Etcd.md)
+ 配置中心
  - [Apollo](apollo/Apollo.md)
  - [Nacos](nacos/Nacos.md)
+ Web软件
  - [Nginx](nginx/Nginx.md)
  - [Apache](apache/Apache.md)
+ 容器化
  - [Docker](docker/Docker.md)
  - [K8s](kubernetes/K8s.md)
+ 操作系统
  - [Linux](linux/Linux.md)
  - [Windows](windows/Windows.md)




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



#### 学习教程
- 官方文档: https://www.php.net/docs.php
- PHP之道: https://learnku.com/docs/php-the-right-way/PHP8.0


#### Web框架
- laravel: 现代化框架
https://laravel.com/
- laravel-s: 介于laravel/lumen与swoole的适配器
https://github.com/hhxsv5/laravel-s
- dingo/api: 基于laravel/lumen框架的restful api包
https://github.com/dingo/api

- Lumen: 
https://lumen.laravel.com/docs/10.x



- yii2-sentry: 适用于Yii2框架的sentry包
https://github.com/notamedia/yii2-sentry

- Yaf: 一个C语言编写的PHP框架
https://www.laruence.com/manual/

- Hyperf
https://hyperf.wiki/3.0/#/
- Hpyerf: 使用docker部署开发环境
https://github.com/hyperf/hyperf-docker

- Swoole: PHP协程框架
https://www.swoole.com/


- PhalApi: 开源接口项目
https://www.phalapi.net/

- Slim: 微框架 
https://www.slimframework.com/

- Workererman: 一款开源高性能PHP应用容器
https://www.workerman.net/

- Phalcon: 基于C扩展的框架
https://phalcon.io/zh-cn


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



#### 相关站点
- composer包仓库
https://packagist.org/

- composer官方站
https://www.phpcomposer.com/


---


### Python



#### 框架
- Django: https://www.djangoproject.com/
- Flask: https://docs.jinkan.org/docs/flask/
- 


#### 第三个类库

- psutil: 查看系统信息(内存,CPU等)
https://github.com/giampaolo/psutil





#### 学习教程

博文
- 官方文档(V3): https://docs.python.org/zh-cn/3/
- 入门教程: http://www.pythondoc.com/pythontutorial3/index.html
- 菜鸟教程(V2,已不推荐): https://www.runoob.com/python/python-tutorial.html
- 菜鸟教程(V3): https://www.runoob.com/python3/python3-mysql.html
- 标准库实例教程: https://learnku.com/docs/pymotw


社区:
- 和鲸社区: https://www.heywhale.com/home/
- 玩蛇网(Python学习与分享平台): https://www.iplaypy.com/

视频课程(免费+付费)
- 风变编程: https://www.pypypy.cn/app#/app-center


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


---

### Rust

- 学习教程
https://github.com/sunface/rust-by-practice



---


### Shell


#### 学习资源
基础-入门
- https://www.runoob.com/linux/linux-shell.html




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


#### 操作系统
- Centos: https://www.centos.org/





- linux的终端可视化工具
https://github.com/sqshq/sampler


- Upx: 文件压缩工具
https://github.com/upx/upx




---


### Windows


#### 相关软件
- Chocolatey: 软件包管理工具
https://chocolatey.org/

- Scoop: 命令行下软件包管理工具(类Mac下的brew)
https://scoop.sh/#/

- Cygwin: 提供windows下的Linux环境
https://www.cygwin.com/index.html



---



### 前端




#### 第三方包
- bce-sdk-js: 对接百度云开发服务接口 
https://baidubce.github.io/bce-sdk-js/





#### 框架
- React
https://www.reactjs.cn/

- Vue
https://cn.vuejs.org/




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


- Virtualbox: 虚拟机软件
https://www.virtualbox.org/



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




## 开发资源汇总
罗列开发中常用的参考文档


### 多种语言学习Bus
- LearnKu: https://learnku.com/


### 微信开发
- 官方文档: https://developers.weixin.qq.com/doc/
- 微信支付: https://pay.weixin.qq.com/wiki/doc/api/index.html
- 微信公众号调试工具: https://mp.weixin.qq.com/debug/cgi-bin/apiinfo
- 微信 JS 接口签名校验工具: https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=jsapisign
- 小程序开放个人申请: https://www.jianshu.com/p/fff515483c6c
- 




## 其他

### 云平台
- 腾讯云: https://cloud.tencent.com/
- 新浪云: https://www.sinacloud.com/
- 阿里云: https://www.aliyun.com/
- 七牛云: https://www.qiniu.com/


### 代码托管
- 腾讯云Coding: https://coding.net/
- 码云: https://gitee.com/
- 



### 学习站
视频
- 51CTO学堂: https://edu.51cto.com/

### 第三方服务
地图类
- 百度地图: https://lbsyun.baidu.com/index.php?title=%E9%A6%96%E9%A1%B5
- 

短信类
- 云片: https://www.yunpian.com/entry
- 腾讯云短信: https://cloud.tencent.com/product/sms



实时通信:
- GoEasy: https://www.goeasy.io/




### 云课程
入门基础
- 阿里云大学: https://edu.aliyun.com/explore/?spm=a2cwt.28120021.J_9305143570.2.13c5704aHcRooO
众多免费课程可以学习,不限于java,python,mysql,linux等,可以看到自己想学习的一些基础教程




### 招聘站
- 智联招聘: https://www.zhaopin.com/
- BOSS: https://www.zhipin.com
- 黄豆纳才: https://zhaopin.clouderwork.com/










