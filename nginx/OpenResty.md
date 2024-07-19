# OpenResty



## 安装

源码包)

```shell
#安装依赖
yum install pcre-devel openssl-devel gcc curl zlib-devel -y

# 下载并解压
wget https://openresty.org/download/openresty-1.25.3.1.tar.gz
tar -zxvf openresty-1.25.3.1.tar.gz

# 编译并安装
cd openresty-1.25.3.1/
./configure
make && make install

# 添加环境变量
vim ~/.bashrc
export PATH=/usr/local/openresty/nginx/sbin:$PATH
source !$
```



## 使用

```shell
# 启动
nginx -c /usr/local/openresty/nginx/conf/nginx.conf
# 配置测试
nginx -t
# 重新加载配置
nginx -s reload


```



### 配置

```shell
```











