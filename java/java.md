# java

## java

### 安装
1.下载源码包并解压
```shell
wget https://repo.huaweicloud.com/java/jdk/8u201-b09/jdk-8u201-linux-x64.tar.gz

tar -zxvf jdk-8u201-linux-x64.tar.gz

mv jdk1.8.0_191 /usr/local/
```

2.配置环境变量
```bash
vim /etc/profile

export JAVA_HOME=/root/jdk1.8.0_201
export CLASSPATH=.:${JAVA_HOME}/jre/lib/rt.jar:${JAVA_HOME}/lib/dt.jar:${JAVA_HOME}/lib/tools.jar
export PATH=$PATH:${JAVA_HOME}/bin

# 配置立即生效
source /etc/profile
```

3.测试
```bash
java -version
```





---

## tomcat

### 安装
1.下载源码
```bash
wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.56/bin/apache-tomcat-9.0.56.tar.gz

tar -xf apache-tomcat-9.0.56.tar.gz -C /usr/local/

mv /usr/local/apache-tomcat-9.0.56 /usr//local/tomcat
```

2.添加配置文件

```bash
vim /etc/profile.d/tomcat.sh

#加入配置
export TOMCAT_HOME=/usr/local/tomcat/

source /etc/profile.d/tomcat.sh
```



## 使用

```bash
#1.启动
/usr/local/tomcat/bin/startup.sh

#2.查看版本信息
/usr/local/tomcat/bin/version.sh

#3.停止服务
/usr/loca/tomcat/bin/shutdown.sh

#4.查看服务
ps -ef|grep tomcat

# 服务启动默认端口：8080
```





