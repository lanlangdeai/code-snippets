# nginx

## 安装

### Yum

```bash
#1.安装依赖	
sudo yum install yum-utils -y

#2.创建文件 /etc/yum.repos.d/nginx.repo 
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true

[nginx-mainline]
name=nginx mainline repo
baseurl=http://nginx.org/packages/mainline/centos/$releasever/$basearch/
gpgcheck=1
enabled=0
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true

  
#By default, the repository for stable nginx packages is used. If you would like to use mainline nginx packages, run the following command:

sudo yum-config-manager --enable nginx-mainline

#3.安装
sudo yum install nginx -y
  
#4.启动nginx
/usr/sbin/nginx
```

安装脚本

```bash
sudo yum install yum-utils -y

tee /etc/yum.repos.d/nginx.repo <<-"EOF"
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true

[nginx-mainline]
name=nginx mainline repo
baseurl=http://nginx.org/packages/mainline/centos/$releasever/$basearch/
gpgcheck=1
enabled=0
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true
EOF

sudo yum install nginx -y

/usr/sbin/nginx
```



### 编译

```bash
#安装依赖:
yum -y install gcc pcre-devel  zlib-devel

#编译安装:
wget https://nginx.org/download/nginx-1.22.1.tar.gz

tar zxvf nginx-1.22.1.tar.gz
cd nginx-1.22.1
./configure
make && make install
```







### 设置自动启动

```bash
#1. 添加系统服务配置文件
vim /lib/systemd/system/nginx.service

#2. 添加配置项
[Unit]
Description=nginx
After=network.target

[Service]
Type=forking
ExecStart=/bin/nginx
ExecReload=/bin/nginx -s reload
ExecStop=/bin/nginx -s quit
PrivateTmp=true

[Install]
WantedBy=multi-user.target

```
配置说明:

```
[Unit]:服务的说明

Description:描述服务
After:描述服务类别

[Service]服务运行参数的设置
Type=forking是后台运行的形式
ExecStart为服务的具体运行命令
ExecReload为重启命令
ExecStop为停止命令
PrivateTmp=True表示给服务分配独立的临时空间

[Install]运行级别下服务安装的相关设置，可设置为多用户，即系统运行级别为3

注意：[Service]的启动、重启、停止命令全部要求使用绝对路径
```





## 使用

常用命令:

```bash
#加入开机启动
systemctl enable nginx

#禁止开机启动
systemctl disable nginx

#启动服务
systemctl start nginx

#停止服务
systemctl stop nginx

#查看服务状态
systemctl status nginx

#查看所有已启动的服务
systemctl list-units -type=service
```

nginx命令

```bash
# 启动服务
/usr/sbin/nginx
  
# 测试配置文件
nginx -t

# 测试配置文件并打印, 方便查看所有的nginx加载的配置文件内容
nginx -T
  
# 停止服务
nginx -s stop
nginx -s quit
  
# 热加载配置文件
nginx -s reload
 
  
# 其他参数
  -v 查看版本
  -V 版本+配置项
  -q  静默方式,不报错
  -c  配置文件地址
```



## 证书

### Cerbot

#### 安装 **snap**

https://snapcraft.io/docs/installing-snap-on-centos

```bash
#查看系统版本
cat /etc/centos-release
  
#centos7
sudo yum install epel-release
  
#centos8
sudo dnf install epel-release
sudo dnf upgrade
  
#安装snap
sudo yum install snapd
  
#systemctl管理
sudo systemctl enable --now snapd.socket
  
#To enable classic snap support
sudo ln -s /var/lib/snapd/snap /snap
```

#### 安装 Certbot

```bash
snap install core
snap refresh core
  
#移除旧安装包
sudo yum remove certbot
  
#安装
sudo snap install --classic certbot
```

#### 添加环境变量

```bash
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

#### 使用

```bash
sudo certbot --nginx
  
#只是生成证书
sudo certbot certonly --nginx
  
#测试自动到期刷新
sudo certbot renew --dry-run
  
 
#查看定时任务:
/etc/crontab/
/etc/cron.*/*
systemctl list-timers
```



## 相关模块

### 添加模块

#### 查看编译使用的参数

```bash
nginx -V
```

#### 添加参数

```bash
--with-http_stub_status_module --with-http_ssl_module --with-http_realip_module


在源码包中执行:
./configure --prefix=/app/nginx -user=nobody -group=nobody --with-http_stub_status_module \
--with-http_ssl_module --with-http_realip_module \
--add-module=../nginx_upstream_hash-0.3.1/ \
--add-module=../gnosek-nginx-upstream-fair-2131c73/
```

#### 重新编译安装

```bash
make
#不要make install，否则就是覆盖安装

cp /app/nginx/sbin/nginx /app/nginx/sbin/nginx.bak
cp ./objs/nginx /app/nginx/sbin/

#然后执行重载:
nginx -s reload
```







## 配置语法

**正则表达式匹配，其中：**

1. \* ~ 为区分大小写匹配
2. \* ~* 为不区分大小写匹配
3. \* !~和!~*分别为区分大小写不匹配及不区分大小写不匹配

**文件及目录匹配，其中：**

1. \* -f和!-f用来判断是否存在文件
2. \* -d和!-d用来判断是否存在目录
3. \* -e和!-e用来判断是否存在文件或目录
4. \* -x和!-x用来判断文件是否可执行

**flag标记有：**

1. \* last 相当于Apache里的[L]标记，表示完成rewrite
2. \* break 终止匹配, 不再匹配后面的规则
3. \* redirect 返回302临时重定向 地址栏会显示跳转后的地址
4. \* permanent 返回301永久重定向 地址栏会显示跳转后的地址

```bash
location ~* /x/glzp {
    return http://xxx.xxx.com/downloadview/index?id=300;
}


location ^~ /site/download/ {
    if ( $query_string ~* "appId=10000024" ) {
        return http://xxx.xxx.com/downloadview/index?id=290;
    }
    proxy_pass http://127.0.0.1:8081;
}


location ^~ /lcmj {
      if ( $query_string ~* ^(.*)$ ){
            return https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxbd3f278c1aeb2ae9&redirect_uri=http://xxx.xxx.com/le/agent/saomalc&response_type=code&scope=snsapi_userinfo&state=$query_string&connect_redirect=1#wechat_redirect;
      }
}
```












## 项目配置

#### python项目

```nginx
server {
    listen  8000;
    server_name localhost;
    access_log  /var/log/nginx/mrdoc_access.log;
    error_log   /var/log/nginx/mrdoc_error.log;

    client_max_body_size 75M;

    location / {
        include /www/MrDoc/deploy/uwsgi_params;
        uwsgi_pass 127.0.0.1:8008;
        uwsgi_read_timeout 60;
    }

    location /static {
        expires 30d;
        autoindex on;
        add_header Cache-Control private;
        alias  /www/MrDoc/static;
    }

    location /media {
        alias  /www/MrDoc/media;
    }
}
```



#### php项目

```nginx
server    {
    listen                          8700;
    server_name                     xxx.xxx.xxx.xxx;
    index                           index.php index.html;
    root                            /data/www/blog/public;
    access_log                      /data/log/nginx/access_8700.log main;
    error_log                       /data/log/nginx/error_8700.log warn;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ .*\.(php|php5)?$
    {
        fastcgi_pass  127.0.0.1:9000;
        fastcgi_index index.php;
        include       fastcgi.conf;  # 加载变量
    }

    location = /robots.txt {
        allow         all;
        log_not_found     off;
        access_log     off;  # 关闭log记录
    }  
    
    location = /favicon.ico {
        expires        max;
        access_log    off;
        # 文件找不到是否进行记录,默认是on,记录
        log_not_found    off;
    }

    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$ {
        expires      30d;  #缓存设置30天
        access_log   off;
    }

    location ~ .*\.(js|css)?$ {
        expires      12h;  # 缓存设置12小时
        access_log   off;
    }

    location ~/\.(?!well-known).* {
        deny all;  # 禁止访问
    }
}

```









#### 非www，默认跳转www地址

```nginx
server {
   listen 80;
   server_name www.xxx.com xxx.com;
   if ($host != 'www.xxx.com') {
       rewrite ^/(.*)$ http://www.xxx.com/$1 permanent;
   }
}
#   permanent – 返回永久重定向的HTTP状态301



server {
      listen                    80;
      server_name      123.com;
      rewrite ^/(.*) http://456.com/$1 redirect;
      access_log off;
}

#   redirect – 返回临时重定向的HTTP状态302

```

#### 生产环境基本配置

```nginx
upstream common {
    server 127.0.0.1:5101;
    server 127.0.0.1:5102;
}
upstream search {
    server 172.16.114.52:5301;
    server 172.16.114.52:5302;
}
limit_req_zone $binary_remote_addr zone=one:10m rate=5r/s;
server {
        listen       80;
        server_name  www.demo.com;
        return       301 https://www.demo.com$request_uri;
}

server {
    listen       443 ssl;
    server_name  www.demo.com;
    ssl on;
    ssl_certificate      /etc/nginx/ssl/demo.com.fullchain.cert;
    ssl_certificate_key  /etc/nginx/ssl/demo.com.key;

    client_max_body_size 20m;  -- 设置的不够大， 文件上传会出现413 Request Entity Too Large
    gzip on;
    limit_req zone=one burst=10;
    access_log  /data0/varlog/nginx/www_demo.access.log  main;
    error_log   /data0/varlog/nginx/www_demo.error.log error;

    if ( $host != 'www.demo.com' ) {
        rewrite ^(.*)$ https://www.demo.com$1 permanent;
    }

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host  $host;
        proxy_set_header X-Real-IP  $remote_addr;
        proxy_set_header X-Forwarded-For  $proxy_add_x_forwarded_for;
    }

    location ~* /fbmain/(common|account|monitor|history_crawl|user|pay|need) {
        proxy_pass_header Server;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_pass http://common;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location ~ /fbmain/search {
        proxy_pass_header Server;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_pass http://search;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        root /data0/wwwroot/nuxt/main_monitor_flask;
    }

    location ~ /static/v1/auto_login {
        proxy_pass_header Server;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_pass http://127.0.0.1:5101;
    }

}
```

#### 证书配置

```ng
   
server {
	
	listen 80; 
	server_name tp5.feekr.com;

	rewrite ^(.*)$  https://$host$1 permanent;
}
  
server {
  
	listen 443; 
	server_name tp5.feekr.com;
	ssl on;
  
	root   /svn/webdata/f/tp5/public;
	index  index.php index.html index.htm;

	ssl_certificate      /web/python/ssl/feekr.pem;
	ssl_certificate_key  /web/python/ssl/feekr.key;
	ssl_session_timeout 5m;
	ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
	ssl_ciphers AESGCM:ALL:!DH:!EXPORT:!RC4:+HIGH:!MEDIUM:!LOW:!aNULL:!eNULL;
	ssl_prefer_server_ciphers on;
		
	location / {
		if (!-e $request_filename) {
			rewrite  ^(.*)$  /index.php?s=/$1  last;
			break;
		}
	}

	location ~ \.php$ {
	
			try_files $uri =404;
            fastcgi_pass  unix:/tmp/php-cgi7.2.sock;
            fastcgi_index index.php;
            include fastcgi.conf;
			
			set $path_info "";
			set $real_script_name $fastcgi_script_name;
			if ($fastcgi_script_name ~ "^(.+?\.php)(/.*)$") {
				set $real_script_name $1;
				set $path_info $2;
			}
			fastcgi_param PATH_INFO $path_info;
			fastcgi_param SCRIPT_FILENAME $document_root$real_script_name;
			fastcgi_param SCRIPT_NAME $real_script_name;
			
	}
	location ~ /\.ht {
		deny  all;
	}
	
}
```





#### 禁止htaccess

```nginx
location ~//.ht {
         deny all;
}
```

#### 禁止访问多目录

```nginx
location ~ ^/(cron|templates)/ {
         deny all;
         break;
 }
 
 可以禁止/data/下多级目录下.log.txt等请求;

location ~ ^/data {
         deny all;
}
```

#### 禁止单个目录

```nginx
location /searchword/cron/ {
         deny all;
 }
 
 单个文件
 location ~ /data/sql/data.sql {
         deny all;
}
```

#### 匹配上传文件目录(展示静态文件)

```nginx
# 会直接将upload追加上  
location ~ ^/upload {
    root "/data/resources/cpc";
}
```





#### 设置过期时间

```nginx
location = /robots.txt {
   allow         all;
   log_not_found     off;  # 不记录404错误日志
   access_log     off;
   expires        99d;  # 99天过期时间
}  

location = /favicon.ico {
   expires        max;
   access_log    off;
   log_not_found    off;
}
```

#### 开启gzip压缩

```
gzip                            on;
gzip_min_length                 1k;
gzip_comp_level                 5;
gzip_buffers                    4 16k;
gzip_http_version        1.1;                                                                                           
gzip_types text/css application/javascript image/png image/jpeg application/x-javascript text/javascript;
gzip_disable                    "MSIE [1-6].";
gzip_vary                       on;
```

#### 访问日志

```nginx
http {
  ...
  log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
        '$status $body_bytes_sent "$http_referer" '
        '"$http_user_agent" "$http_x_forwarded_for" "$request_time" "$upstream_response_time"';
}

# 这里注意   记录了request_time  和upstream_response_time  两个时间
request_time:指的就是从接受用户请求的第一个字节到发送完响应数据的时间，即包括接收请求数据时间、程序响应时间、输出响应数据时间。
upstream_response_time:是指从 nginx 向后端（php-cgi)建立连接开始到接受完数据然后关闭连接为止的时间。
```

#### 非HTTP跳转https

```nginx
server {
    listen 80;
    server_name www.域名.com;
    rewrite ^(.*)$ https://${server_name}$1 permanent; 
}

server {
    listen 443;
    server_name www.域名.com;
    root /home/wwwroot;
    ssl on;
    ssl_certificate /etc/nginx/certs/server.crt;
    ssl_certificate_key /etc/nginx/certs/server.key;
    ....
}


---


## 常见问题
1.访问日志中有大量的head请求，处理方式
```nginx
server{
	if ($request_method ~ ^(HEAD)$ ) {
		return 200 "All OK";
	}
}
```

#### 处理head请求

```bash
server{
	if ($request_method ~ ^(HEAD)$ ) {
		return 200 "All OK";
	}
}
```

#### 处理Option预检请求(或在项目中进行处理, 否则会出现Option也可以正常请求数据的情况)

```bash
add_header Access-Control-Allow-Origin '*' always;
add_header Access-Control-Allow-Headers '*';
add_header Access-Control-Allow-Methods '*';
add_header Access-Control-Allow-Credentials 'true';
if ($request_method = 'OPTIONS') {
   return 204;
}
```





#### Proxy_set_header 设置

```bash
location / {
		proxy_pass http://127.0.0.1:3000;
		proxy_set_header Host  $host;
    proxy_set_header X-Real-IP  $remote_addr;
    proxy_set_header X-Forwarded-For  $proxy_add_x_forwarded_for;
	}
```

#### 限制单个IP的访问频率

```bash
http {

    #$limit_conn_zone：限制并发连接数
    limit_conn_zone $binary_remote_addr zone=one1:10m;

    #limit_req_zone：请求频率
    #$binary_remote_addr：以客户端IP进行限制
    #zone=one:10m：创建IP存储区大小为10M,用来存储访问频率
    #rate=10r/s：表示客户端的访问评率为每秒10次
    limit_req_zone $binary_remote_addr zone=one2:10m   rate=10r/s;
     
}   


# server配置

server {
        listen       80;
        server_name  localhost;
       

        location / {
            #限制并发数2
            limit_conn  one1  2;  
            #burst：如果请求的频率超过了限制域配置的值，请求处理会被延迟
            #nodelay：超过频率限制的请求会被延迟，直到被延迟的请求数超过了定义的阈值，这个请求会被终止，并返回503
            limit_req   zone=one2 burst=10 nodelay;
            root   html;
            index  index.html index.htm;
        }

}
```













