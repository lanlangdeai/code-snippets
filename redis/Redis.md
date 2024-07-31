# Redis



## 安装

### 源码

```shell
# 下载源码包
wget http://download.redis.io/releases/redis-6.2.6.tar.gz
# 解压
tar -xf redis-6.2.6.tar.gz
cd redis-6.2.6

# 编译
## 在src路径下编译源码, 生成redis-cli和redis-server
make

# 复制环境到指定路径完成安装
cp -r ~/redis-6.2.6 /usr/local/redis

# 后台运行配置修改
vim /usr/local/redis/redis.conf
## 修改
daemonize yes

# 建立软连接
ln -s /usr/local/redis/src/redis-server /usr/bin/redis-server
ln -s /usr/local/redis/src/redis-cli /usr/bin/redis-cli

# 运行
cd /usr/local/redis
redis-server ./redis.conf
```

5.x版本

```bash
wget https://download.redis.io/releases/redis-5.0.14.tar.gz
tar -zxvf redis-5.0.14.tar.gz
cd redis-5.0.14

make
make install PREFIX=/usr/local/redis
cp redis.conf /usr/local/redis/
#启动服务
/usr/local/redis/bin/redis-server /usr/local/redis/redis.conf

在/etc/profile 添加全局环境变量
export PATH=$PATH:/usr/local/redis/bin
```

### Docker

```bash
docker run --name redis-server -d -p 127.0.0.1:6379:6379 redis:5.0.14-alpine
```







## 配置

```
daemonize yes   后台运行
bind   绑定的IP, 端口
requirepass 密码
```









## 使用

```shell
# 连接
redis-cli

# 关闭服务
pkill -f redis -9
## 或
redis-cli  shutdown

```



## 部署

#### 加入系统服务

vim /etc/systemd/system/redis.service

```bash
[Unit]
Description=redis-server
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/bin/redis.conf
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

使用:

```bash
systemctl daemon-reload
systemctl start redis.service
systemctl enable redis.service
```





#### 命令全局使用

```bash
ln -s /usr/local/redis/bin/redis-cli /usr/bin/redis-cli
```

