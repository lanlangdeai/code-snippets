# Redis



## 安装

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



## 使用

```shell
# 连接
redis-cli

# 关闭服务
pkill -f redis -9
## 或
redis-cli  shutdown

```



