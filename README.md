# Code-Snippets

  本人从事一线开发将近多年时间(2016~至今),以下罗列的都是本人开发生涯中所涉猎的技术栈,汇总于此.
希望可以帮助更多开发者,或是初入编程,或是编程老兵都可以有所获,不限于代码,开发思路,架构思想,开发周边服务等等

## 知识结构

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
## 面试题

* [网络面试题](other/network-interview.md)

* [Redis面试题](redis/redis-interview.md)

* [MySQL面试题](mysql/mysql_interview.md)




---

## [PHP](https://www.php.net/manual/zh/)

Windows下的站点: https://windows.php.net, 对应扩展: https://windows.php.net/downloads/pecl/releases/



#### 环境搭建

本地开发

- Xampp(window+mac)
https://www.apachefriends.org/

- PhpStudy
https://www.xp.cn/

- ServBay(Mac)
https://www.servbay.dev/zh_CN

- 宝塔
  https://www.bt.cn/new/index.html

- UpUpW(Windows, 较新版本不支持)

  https://www.upupw.net/



linux


- Lnmp

  https://lnmp.org/

- 



#### 学习教程
- 官方文档: https://www.php.net/docs.php
- PHP之道: https://learnku.com/docs/php-the-right-way/PHP8.0
- Learnku: https://learnku.com/laravel
- PHPChina: http://www.phpchina.com/



#### 不错的博客

- 鸟哥: https://www.laruence.com/
- https://www.yuque.com/u30882/uqzhpb
- 傲雪星枫:https://blog.csdn.net/fdipzone





#### Web框架

- laravel: 现代化框架
https://laravel.com/
- laravel-s: 介于laravel/lumen与swoole的适配器
https://github.com/hhxsv5/laravel-s
- dingo/api: 基于laravel/lumen框架的restful api包
https://github.com/dingo/api

- Lumen: 
  https://lumen.laravel.com/docs/10.x

- ThinkPHP:大道至简

​	https://www.thinkphp.cn/

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

- Easyswoole: 企业级分布式协程框架

  https://www.easyswoole.com/

- CI: 小巧

  https://codeigniter.org.cn/


- PhalApi: 开源接口项目
https://www.phalapi.net/

- Slim: 微框架 
https://www.slimframework.com/

- Workererman: 一款开源高性能PHP应用容器
https://www.workerman.net/

- Phalcon: 基于C扩展的框架
  https://phalcon.io/zh-cn

- MeepoPS: 高效的PHP Socket服务

  http://meepops.lanecn.com/

- CachePHP:

​	https://cakephp.org/



#### 系统类库

- ZipArchive: zip压缩







#### 第三方类库

- laravel-uuid: 生成uuid
https://github.com/webpatser/laravel-uuid

- sso: SSo实现包
https://github.com/evangui/sso


- oauth2: OAUTH2.0实现
https://github.com/thephpleague/oauth2-client

- OpenID: OpenId连接授权
  https://github.com/jumbojett/OpenID-Connect-PHP

- phpredis: 操作Redis的扩展库

  https://github.com/phpredis/phpredis

- SeasLog: 日志记录(需要)

  https://github.com/SeasX/SeasLog

- Guzzle: 发送网络请求

  https://docs.guzzlephp.org/en/stable/

- QueryList: dom解析

​	https://querylist.cc/

- NotORM: 非常简单操作数据库的类

  https://www.notorm.com/
  
- PhpSpreadsheet: Excel操作库

https://github.com/PHPOffice/PhpSpreadsheet.git

- FPID: PDF操作库

  https://github.com/Setasign/FPDI

- mpdf: pdf操作库

  https://mpdf.github.io/

- phpqrcode: 二维码库

http://phpqrcode.sourceforge.net/



> 更多: [packagist](/php/packagist.md)
>

- Sphinx: 搜索服务

  http://sphinxsearch.com/

- PHPUnit: 单元测试

  https://phpunit.de/index.html

- symfony/mailer: 邮件发送

  https://symfony.com/doc/current/mailer.html
  
- PHPMailer: 邮件发送

  https://github.com/PHPMailer/PHPMailer

- Mobile-Detect: 终端检测 

  https://github.com/serbanghita/Mobile-Detect














#### 相关工具
- 项目发布工具
https://github.com/REBELinBLUE/deployer

- xdebug: 代码调试/debug
  https://github.com/xdebug/xdebug


- Composer镜像源切换工具
  https://github.com/slince/composer-registry-manager

- #### awesome-php: 收集整理一些常用的PHP类库, 资源以及技巧

​	https://github.com/JingwenTian/awesome-php







#### 相关站点

##### composer镜像

https://pkg.xyz/

##### composer包仓库

https://packagist.org/

##### composer官方站

https://www.phpcomposer.com/



#### 解决方案

	- xunsearch: 全文检索技术方案

​	http://www.xunsearch.com/



#### 相关开源项目

- VueThink: https://github.com/honraytech/VueThink

- FastAdmin: ThinkPHP+Bootstrap开发的快速后台开发框架

  https://www.fastadmin.net/

- YOf: yaf教程

  https://github.com/xwmhmily/YOF






---


## Python



#### 框架
- Django: https://www.djangoproject.com/
- Flask: https://docs.jinkan.org/docs/flask/



#### 系统类库

- argparse: 命令行解析

https://docs.python.org/zh-cn/3.9/library/argparse.html?highlight=argparse#module-argparse

- shelve,dbm:本地数据存储
- time: 时间相关
- datetime: 日期相关
- string: 字符串相关
- logging: 日志相关
- csv: CSV格式数据处理
- linecache: 文件读取




#### 第三个类库

- psutil: 查看系统信息(内存,CPU等)
  https://github.com/giampaolo/psutil
- configparser: ini文件读写

​		https://docs.python.org/zh-cn/3.9/library/configparser.html

- requests: 网络请求库

​		https://github.com/psf/requests







#### 学习教程

##### 博文

- 官方文档(V3): https://docs.python.org/zh-cn/3/
- 入门教程: http://www.pythondoc.com/pythontutorial3/index.html
- 菜鸟教程(V2,已不推荐): https://www.runoob.com/python/python-tutorial.html
- 菜鸟教程(V3): https://www.runoob.com/python3/python3-mysql.html
- 标准库实例教程: https://learnku.com/docs/pymotw
- 入门教程: https://python.archgrid.xyz/
- Scrapy: https://scrapy-chs.readthedocs.io/zh-cn/1.0/intro/tutorial.html
- PyQt: https://maicss.com/pyqt/
- 廖雪峰: https://www.liaoxuefeng.com/wiki/1016959663602400

##### 社区:

- 和鲸社区: https://www.heywhale.com/home/
- 玩蛇网(Python学习与分享平台): https://www.iplaypy.com/

- 风变编程: https://www.pypypy.cn/app#/app-center
- 中文开发者社区: https://www.pythontab.com/



#### 面试资源

- https://github.com/kenwoodjw/python_interview_question




---


## Golang



#### 教程

梯子教程网: https://www.tizi365.com/



#### 博文

- https://www.liwenzhou.com/



#### 在线工具

- json-to-go: https://mholt.github.io/json-to-go/





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
- **go-redis**: Redis客户端包2
https://github.com/redis/go-redis

- mongo-go-driver: MongoDB客户端
https://github.com/mongodb/mongo-go-driver

- nsq: 分布式消息平台
https://github.com/nsqio/nsq


- **cobra**: Cli应用程序库(类Python中的Click)
https://github.com/spf13/cobra

- **pflag**: 程序参数处理(类Python中的argparse) 
https://github.com/spf13/pflag

- **shopspring/decimal**: 浮点数精度处理
https://github.com/shopspring/decimal

- **copier**: 结构体/切片/映射的复制
https://github.com/jinzhu/copier


- **cast**: 从一个类型转换为另一种类型
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


- **json-iterator/go**: 高效的JSON序列化工具
  https://github.com/json-iterator/go

- sonic: 一个速度奇快的 JSON 序列化/反序列化库
https://github.com/bytedance/sonic


- gjon: json数据解析
https://github.com/tidwall/gjson


- prometheus/client_golang: prometheus的golang语言客户端包
https://github.com/prometheus/client_golang

- gin-contrib/pprof: gin框架的pprof中间件
https://github.com/gin-contrib/pprof

- **gin-swagger**: gin框架生成swagger文档中间件
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

- **cron**: 定时任务
https://github.com/robfig/cron

- **日志分割**
https://github.com/natefinch/lumberjack


- **zap**: 日志管理工具
https://github.com/uber-go/zap
- logrus: 日志管理工具
https://github.com/sirupsen/logrus
- zerolog: 日志管理工具
https://github.com/rs/zerolog

- converter: mysql表结构自动生成golang struct
https://github.com/gohouse/converter

- gorequest: 发起http网络请求
https://github.com/parnurzeal/gorequest
- resty: 发起http网络请求
https://github.com/go-resty/resty


- **viper**: 配置管理
https://github.com/spf13/viper

- cleanenv: 纯净配置管理工具
https://github.com/ilyakaznacheev/cleanenv

- gopsutil: 查看系统信息(内存,CPU)
https://github.com/shirou/gopsutil


- **go-qrcode**: 生成二维码
https://github.com/skip2/go-qrcode

- **mimetype**: 探测媒体,文件的类型
https://github.com/gabriel-vasile/mimetype


- wecom-go-sdk: 企业微信应用接入
https://github.com/go-laoji/wecom-go-sdk


- pretty: 友好打印JSON
https://github.com/tidwall/pretty

- **lo**: 高效友好的处理slice,map,math,string,tuple,channel
https://github.com/samber/lo 

- **lancet**: 通用工具库
https://github.com/duke-git/lancet

- excelize: Excel表格处理
https://github.com/qax-os/excelize

- jinzhu/now: 时间工具
https://github.com/jinzhu/now

- **carbon**: 时间/日期扩展库
https://github.com/golang-module/carbon





#### Web框架

- Echo
https://github.com/labstack/echo
https://echo.labstack.com/
- Gin

​	https://github.com/teris-io/shortid

- GoFrame

方文档: https://goframe.org/pages/viewpage.action?pageId=1114119

Github: https://github.com/gogf/gf




#### 微服务
- go-kit
https://github.com/go-kit/kit


- hertz: 字节推出的微服务框架
https://github.com/cloudwego/hertz

- kratos: 哔哩哔哩推出的微服务框架
  https://github.com/go-kratos/kratos

- gRPC:

​		https://grpc.io/



#### Github
##### Golang学习

  - https://github.com/jiujuan/go-collection
  - https://github.com/sdgmf/go-project-sample
  - https://github.com/jincheng9/go-tutorial
  - https://github.com/golang/example

##### 进阶学习(成熟项目+优秀借鉴)

  - https://github.com/xinliangnote/go-gin-api
  - https://www.gin-vue-admin.com/

##### 后台系统

| 项目地址                               | 说明                |      |
| -------------------------------------- | ------------------- | ---- |
| https://github.com/tiger1103/gfast.git | 后台系统-golang+vue |      |
|                                        |                     |      |
|                                        |                     |      |



##### 代理池搭建

  - https://github.com/henson/proxypool

##### 博客平台搭建

  - https://github.com/go-sonic/sonic

##### 静态网站生成器Hugo

  - https://www.gohugo.org/



##### 代码风格

- https://github.com/uber-go/guide
Go项目结构
- https://github.com/golang-standards/project-layout
- https://github.com/evrone/go-clean-template



##### 代码检测工具

- https://github.com/golangci/golangci-lint
Go-Build模版
- https://github.com/thockin/go-build-template



#### 面试
- https://github.com/lifei6671/interview-go


---



## [NodeJS](https://nodejs.org/zh-cn)



#### 周边工具

- [npm](https://www.npmjs.com/)



#### 相关项目

- hexo:博客系统

   https://hexo.io/zh-cn/docs/



#### Github开源项目

- 商城小店: https://github.com/iamdarcy/hioshop-admin
- 



---





## 前端

Nodejs: https://nodejs.org/en



#### 知识矩阵

- Less: https://www.runoob.com/manual/lessguide/


- element-ui: https://element.eleme.cn/#/zh-CN
- AT-UI: https://at-ui.github.io/at-ui/#/zh



#### 第三方包

- yarn: https://yarnpkg.com/
- JQuery:
  - 懒人之家:https://www.lanrenzhijia.com/jquery/
  - jQuery之家:https://www.jq22.com/

- bce-sdk-js: 对接百度云开发服务接口 
  https://baidubce.github.io/bce-sdk-js/


- clipboard.js: 复制粘贴板
  https://clipboardjs.com/

- Swiper: 滑动特效
  https://www.swiper.com.cn/

- 瀑布流
  https://masonry.desandro.com/

- 图片,视频悬浮展示
  https://fancyapps.com/fancybox/
  
- Share.js 一键分享

  http://overtrue.me/share.js/

- 基于css的效果
  https://animate.style/
  http://ianlunn.github.io/Hover/
  https://elrumordelaluz.github.io/csshake/

- 基于JS的效果
  http://anijs.github.io/

更多插件: https://www.bootcdn.cn/



#### 框架

- React
  https://www.reactjs.cn/

- Vue
  https://cn.vuejs.org/

- Element-UI

  https://element.eleme.cn/#/zh-CN

- vue-element-admin

  https://github.com/PanJiaChen/vue-element-admin

  




- 字体图标
  https://github.com/ryanoasis/nerd-fonts

- UI组件库

  https://at-ui.github.io/at-ui/#/zh

  



#### 工具

- json文件查看与管理工具
  https://github.com/triggerdotdev/jsonhero-web



#### 效果站点(可借鉴的效果,功能点,交互)

- https://isux.tencent.com/



#### 学习教程

- https://www.w3cways.com/
- w3school: https://www.w3school.com.cn/
- 

#### Github项目借鉴

移动端方案:

- [一个基于 Vue 3 生态系统的移动 web 应用模板](https://github.com/easy-temps/vue3-vant-mobile)
- [一个移动端 H5 商城](https://github.com/JoeshuTT/v-shop) 存在vue2和vue3两个版本
- [vue搭建移动端开发,基于vue-cli4.0+webpack 4+vant ui + sass+ rem适配方案+axios封装](https://github.com/sunniejs/vue-h5-template)
- [基于 vue3 + vant3 的 H5移动端 demo]() 







---



## Rust

- 学习教程
https://github.com/sunface/rust-by-practice







---


## Shell


#### 学习资源
基础-入门
- https://www.runoob.com/linux/linux-shell.html


---









---



## [Lua](https://www.lua.org/)







---



## MySQL







---

## MongoDB



相关博文:

- https://www.cnblogs.com/chenmh
- 中文社区: https://mongoing.com/







---

## ClickHouse
官方地址: https://clickhouse.com/docs/zh







## [Redis](https://redis.io/)

中文网: https://www.redis.net.cn/



- 布隆过滤器模块
https://github.com/RedisBloom/RedisBloom


---



## 消息队列

#### [Kafka](https://hexo.io/zh-cn/docs/)





## Prometheus

#### 学习教程

- https://yunlzheng.gitbook.io/prometheus-book/parti-prometheus-ji-chu/promql/prometheus-promql-best-praticase





---





## Nginx



相关教程:

- https://tengine.taobao.org/book/index.html
- 



---







## [Docker](https://www.docker.com/)



#### 学习教程

- https://www.qikqiak.com/k8s-book/
- https://yeasy.gitbook.io/docker_practice/kubernetes/concepts
- [https://www.qikqiak.com/k8s-book/docs/18.YAML%20%E6%96%87%E4%BB%B6.html](https://www.qikqiak.com/k8s-book/docs/18.YAML 文件.html)





---





## K8s


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
- https://github.com/bregman-arie/devops-exercises?mode=light



## DevOps



### 部署工具

- bytebase: devpos 平台
https://github.com/bytebase/bytebase
- Walle: 项目代码部署工具

​	https://walle-web.io/index.html



### [Jenkins](https://www.jenkins.io/)






### 学习教程
- https://github.com/bregman-arie/devops-exercises

Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoSQL, Azure, GCP, DNS, Elastic, Network, Virtualization. DevOps Interview




---


## Linux


#### 操作系统
- Centos: https://www.centos.org/





- linux的终端可视化工具
https://github.com/sqshq/sampler


- Upx: 文件压缩工具
https://github.com/upx/upx



相关教程:

- Linux工具: https://linuxtools-rst.readthedocs.io/zh-cn/latest/index.html
- 






---


## Windows


#### 相关软件
##### Chocolatey: 软件包管理工具

https://chocolatey.org/



##### Scoop: 命令行下软件包管理工具(类Mac下的brew)

https://scoop.sh/#/



##### Cygwin: 提供windows下的Linux环境

https://www.cygwin.com/index.html



##### Vagrant: 构建虚拟开发环境的工具

https://www.vagrantup.com/

vagrant包: http://www.vagrantbox.es/









---



- 




---


## 机器学习

- https://github.com/microsoft/ML-For-Beginners





## 人工智能(AI)

相关项目:

- dify





## 编辑器

IDE使用教程(PHPstorm,Pycharm,Goland,WebStorm,DataGrip等)
- https://github.com/judasn/IntelliJ-IDEA-Tutorial
- [phpstorm](https://www.jetbrains.com/zh-cn/phpstorm/)



注: 激活码http://idea.lanyus.com/


---



## 周边服务

[IP]
1. https://www.ipip.net


---



## 使用软件&工具

#### typora-activation: Typora激活工具

https://github.com/markyin0707/typora-activation

#### Virtualbox: 虚拟机软件

https://www.virtualbox.org/

#### Xshell+Xftp

https://www.xshell.com/zh/



#### Etcd的可视化客户端

https://github.com/gtamas/etcdmanager

#### Zookeeper GUI工具

https://github.com/vran-dev/PrettyZoo

#### uPic: 图片上传工具(Mac)

https://github.com/gee1k/uPic

#### Cloudreve: 云盘系统

https://github.com/cloudreve/Cloudreve

#### 代码片段管理软件

https://github.com/massCodeIO/massCode



#### wrk: 性能测试工具

https://github.com/wg/wrk

#### log.io: 实时日志监控工具

https://github.com/NarrativeScience/log.io

#### GoAccess: 日志分析工具

https://goaccess.io/




---



## 平台类

- 静态导航网站
https://github.com/WebStackPage/WebStackPage.github.io

- 站点监控工具(Uptime)
https://github.com/louislam/uptime-kuma


---



## 公共资源列表

- Etcd: https://github.com/etcd-io/etcd
- Apollo: https://github.com/apolloconfig/apollo-quick-start
- Proto Buffer: https://github.com/protocolbuffers/protobuf
- 

---



## 码如人生

- 程序员的副业: https://github.com/easychen/lean-side-bussiness
- 


---



## 开发资源汇总

罗列开发中常用的参考文档


### 多种语言学习Bus
- LearnKu: https://learnku.com/


### 微信开发
- 官方文档: https://developers.weixin.qq.com/doc/
- 微信支付: https://pay.weixin.qq.com/wiki/doc/api/index.html
- 微信公众号在线调试工具: https://mp.weixin.qq.com/debug/cgi-bin/apiinfo
- 微信 JS 接口签名校验工具: https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=jsapisign
- 小程序开放个人申请: https://www.jianshu.com/p/fff515483c6c
- 微信Web开发者工具: https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Web_Developer_Tools.html
- 历史版本: https://weixin.qq.com/cgi-bin/readtemplate?lang=zh_CN&t=weixin_faq_list&head=true
- 开启开发者工具: https://github.com/JaveleyQAQ/WeChatOpenDevTools-Python





## Github开源项目

网页分析: https://github.com/umami-software/umami

监控工具: https://github.com/louislam/uptime-kuma

数据面板平台: https://github.com/appsmithorg/appsmith

Bi数据分析: https://github.com/getredash/redash



### 工具&软件

github文件下载加速: https://mirror.ghproxy.com/

 



## 不错的博客

- https://www.helloweba.net/
- https://www.php20.cn/
- https://imququ.com/
- 

### 博客周边

- 角标: https://tholman.com/github-corners/?spm=a2c4e.11153940.blogcont362865.19.7ad64508EPW4EO





## 问题搜索

站点

- https://stackoverflow.com/questions
- 




---

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
#### 视频

- 51CTO学堂: https://edu.51cto.com/
- 极客学院:https://www.jikexueyuan.com/



#### 文档

- 稀土掘金: https://juejin.cn/
- 



#### 教程

- 迹忆客: https://www.jiyik.com/
- tutsplus: https://code.tutsplus.com/
- 即学即码:http://www.jixuejima.cn/



### 博文站

- InfoQ: https://www.infoq.cn/



### 技术靶场

- 代码战争: https://www.codewars.com/
- 力扣: https://leetcode.cn/
- 




### 第三方服务
#### 地图类

- 百度地图: https://lbsyun.baidu.com/index.php?title=%E9%A6%96%E9%A1%B5
- 

#### 短信类

- 云片: https://www.yunpian.com/entry
- 腾讯云短信: https://cloud.tencent.com/product/sms

#### 存储类(OSS)

- 又拍云: https://www.upyun.com/
- 阿里云:
- 七牛云:https://www.qiniu.com/prices/kodo
- R2: https://developers.cloudflare.com/r2/pricing

#### 实时通信:

- GoEasy: https://www.goeasy.io/

#### 音视频服务:

- 融云: https://www.rongcloud.cn/



#### 检测类: 微信域名,链接封禁状态,证书过期检测,QQ检测等

- 极强检测: https://www.urlzt.com/
- https://www.rrbay.com

#### IP代理

- 快代理: https://www.kuaidaili.com/free/



#### 数据

- 数数科技: https://thinkingdata.cn/



#### 能力

- 讯飞开放平台: https://www.xfyun.cn/
- 火山引擎: https://www.volcengine.com/




### 云课程
入门基础
- 阿里云大学: https://edu.aliyun.com/explore/?spm=a2cwt.28120021.J_9305143570.2.13c5704aHcRooO
众多免费课程可以学习,不限于java,python,mysql,linux等,可以看到自己想学习的一些基础教程



中级

- 码神之路: https://mszlu.com/

​	Java,Go,Rust等




### 招聘站
- 智联招聘: https://www.zhaopin.com/

- BOSS: https://www.zhipin.com

- 黄豆纳才: https://zhaopin.clouderwork.com/

  


### 项目开发

#### 团队协作工具

- Tower: https://tower.im/
- Zoho WorkDrive: https://www.zoho.com.cn/
- 禅道: http://zenpms.cn/

#### 敏捷开发

- tapd: https://www.tapd.cn/
- trello: https://trello.com/
- tower: https://tower.im



#### 代码管理

- 自建: Gitlab,[Gogs](https://gogs.io/)

- 第三方平台: 阿里云,腾讯云,码云,rap2等

  

#### 接口管理

- 自建: Yapi,postman
- 第三方: [showdoc](https://www.showdoc.com.cn/),Apifox
- [eolink](https://www.eolink.com/)
- Rap2: http://rap2.taobao.org/

#### 文档输出

- [腾讯文档](https://docs.qq.com/)
- 钉钉文档
- wps
- [金山文档](https://www.wps.cn/)
- Zoho: https://www.zoho.com.cn/workdrive/



#### 知识库

- Confluence
- 飞书文档
- 看云



#### 产品设计

- [蓝湖](https://lanhuapp.com)

项目工程



#### 错误日志监控告警平台

- Sentry: https://sentry.io/welcome/
- fundebug - 前端bug上报: https://www.fundebug.com/



#### 质量检测

- SonarQube: https://www.sonarsource.com/products/sonarqube/



#### 堡垒机

- jumpserver



#### 科学上网

- [iguge](https://iguge.net/)



#### 开发日常工具

- 加解密等工具: https://gchq.github.io/CyberChef/



## 附录

- 正则表: http://www.jb51.net/shouce/jquery1.82/regexp.html
- ASCII码表: https://www.asciitable.com/

![ASCII](E:\lanlang\code-snippets\img\ascii1.gif)

![ASCII2](E:\lanlang\code-snippets\img\ascii2.gif)



#### URL编码对照表

| backspace | 8%   | A    | 41%  | a    | 61%  | §    | %A7  | Õ    | %D5  |      |
| --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| tab       | 9%   | B    | 42%  | b    | 62%  | «    | %AB  | Ö    | %D6  |      |
| linefeed  | %0A  | C    | 43%  | c    | 63%  | ¬    | %AC  | Ø    | %D8  |      |
| creturn   | %0D  | D    | 44%  | d    | 64%  | ¯    | %AD  | Ù    | %D9  |      |
| space     | 20%  | E    | 45%  | e    | 65%  | º    | %B0  | Ú    | %DA  |      |
| !         | 21%  | F    | 46%  | f    | 66%  | ±    | %B1  | Û    | %DB  |      |
| "         | 22%  | G    | 47%  | g    | 67%  | ª    | %B2  | Ü    | %DC  |      |
| #         | 23%  | H    | 48%  | h    | 68%  | ,    | %B4  | Ý    | %DD  |      |
| $         | 24%  | I    | 49%  | i    | 69%  | µ    | %B5  | Þ    | %DE  |      |
| %         | 25%  | J    | %4A  | j    | %6A  | »    | %BB  | ß    | %DF  |      |
| &         | 26%  | K    | %4B  | k    | %6B  | ¼    | %BC  | à    | %E0  |      |
| '         | 27%  | L    | %4C  | l    | %6C  | ½    | %BD  | á    | %E1  |      |
| (         | 28%  | M    | %4D  | m    | %6D  | ¿    | %BF  | â    | %E2  |      |
| )         | 29%  | N    | %4E  | n    | %6E  | À    | %C0  | ã    | %E3  |      |
| *         | %2A  | O    | %4F  | o    | %6F  | Á    | %C1  | ä    | %E4  |      |
| +         | %2B  | P    | 50%  | p    | 70%  | Â    | %C2  | å    | %E5  |      |
| ,         | %2C  | Q    | 51%  | q    | 71%  | Ã    | %C3  | æ    | %E6  |      |
| -         | %2D  | R    | 52%  | r    | 72%  | Ä    | %C4  | ç    | %E7  |      |
| .         | %2E  | S    | 53%  | s    | 73%  | Å    | %C5  | è    | %E8  |      |
| /         | %2F  | T    | 54%  | t    | 74%  | Æ    | %C6  | é    | %E9  |      |
| 0         | 30%  | U    | 55%  | u    | 75%  | Ç    | %C7  | ê    | %EA  |      |
| 1         | 31%  | V    | 56%  | v    | 76%  | È    | %C8  | ë    | %EB  |      |
| 2         | 32%  | W    | 57%  | w    | 77%  | É    | %C9  | ì    | %EC  |      |
| 3         | 33%  | X    | 58%  | x    | 78%  | Ê    | %CA  | í    | %ED  |      |
| 4         | 34%  | Y    | 59%  | y    | 79%  | Ë    | %CB  | î    | %EE  |      |
| 5         | 35%  | Z    | %5A  | z    | %7A  | Ì    | %CC  | ï    | %EF  |      |
| 6         | 36%  |      |      |      |      |      |      | ð    | %F0  |      |
| 7         | 37%  | ?    | %3F  | {    | %7B  | Í    | %CD  | ñ    | %F1  |      |
| 8         | 38%  | @    | 40%  | \|   | %7C  | Î    | %CE  | ò    | %F2  |      |
| 9         | 39%  | [    | %5B  | }    | %7D  | Ï    | %CF  | ó    | %F3  |      |
| :         | %3A  | \    | %5C  | ~    | %7E  | Ð    | %D0  | ô    | %F4  |      |
| ;         | %3B  | ]    | %5D  | ¢    | %A2  | Ñ    | %D1  | õ    | %F5  |      |
| <         | %3C  | ^    | %5E  | £    | %A3  | Ò    | %D2  | ö    | %F6  |      |
| =         | %3D  | _    | %5F  | ¥    | %A5  | Ó    | %D3  | ÷    | %F7  |      |
| >         | %3E  | `    | 60%  | \|   | %A6  | Ô    | %D4  | ø    | %F8  |      |
|           |      |      |      |      |      |      |      | ù    | %F9  |      |
