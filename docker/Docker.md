# Docker

## 安装
[docker]

1.卸载老版本
```bash
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

```

2.添加包管理

```bash
sudo yum install -y yum-utils  device-mapper-persistent-data lvm2
sudo yum-config-manager \
  --add-repo \
  https://download.docker.com/linux/centos/docker-ce.repo
# 若失败,则使用阿里云镜像
yum-config-manager \
    --add-repo \
    https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
# Centos7)    
yum makecache fast
# Centos8)
dnf makecache
```

3.安装
```bash
sudo yum install docker-ce docker-ce-cli containerd.io -y

# 可以查看并安装指定版本
yum list docker-ce --showduplicates | sort -r  #查看版本
sudo yum install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io #安装指定版本
```

4.常用命令

```bash
# 启动服务
sudo systemctl start docker
# 设置开机启动
sudo systemctl enable docker
# 重载配置
sudo systemctl daemon-reload
# 重启服务
systemctl restart docker


```



[docker-compose]

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 添加权限
chmod +x /usr/local/bin/docker-compose
```



安装脚本

```bash
#!/bin/bash
## 需要切换到root下
yum install yum-utils device-mapper-persistent-data lvm2 -y

yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce -y

# 镜像加速
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-EOF
{
  "registry-mirrors": [
    "https://registry.docker-cn.com",
    "http://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn"
  ]
}
EOF
systemctl daemon-reload
systemctl enable docker
systemctl start docker


# 安装docker-compose
curl -L https://get.daocloud.io/docker/compose/releases/download/1.29.0/docker-compose-$(uname -s)-$(uname -m) > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

```





## 镜像加速

```bash
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://pb84l2li.mirror.aliyuncs.com"]
}
EOF

sudo systemctl daemon-reload
sudo systemctl restart docker

```

## 常用命令
```bash

```

## 参数说明
```text
-d  
    后台运行

--name=定义服务名称
    

-p 5800:5800  
    端口映射，宿主机端口：容器端口

--shm-size 1g   
    设置共享内存大小

-e  DISPLAY_WIDTH=1366  
    设置环境变量

--privileged=true 
    享有特权

```



---

## Dockerfile

### 语法说明
```Dockerfile



# NGINX服务
FROM ubuntu
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g'  /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y nginx
COPY index.html  /var/www/html
ENTRYPOINT ["/usr/bin/nginx", "-g", "daemon off;"]
EXPOSE 80

```

### 语法参数说明
```text
- FROM
    一般除了注释会放到第一行， 表示该镜像的基础镜像

- MAINTAINER
    标识维护人的信息， 可以后面添加维护者的名称

- RUN
    执行一条命令

- COPY
    进行文件的拷贝

- ENTRYPOINT
    标识命令文件的入点

- EXPOSE
    标识暴露的端口
```







