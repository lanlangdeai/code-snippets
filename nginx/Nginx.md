# nginx

## 安装&使用
[安装]


设置自动启动
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


[使用]
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




## 模版

python项目
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


## 示例
1.非www，默认跳转www地址
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

2. 生产环境基本配置

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

3. 禁止htaccess

```nginx
location ~//.ht {
         deny all;
}
```

4.禁止访问多目录

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

5.禁止单个目录

```nginx
location /searchword/cron/ {
         deny all;
 }
 
 单个文件
 location ~ /data/sql/data.sql {
         deny all;
}
```

6.设置过期时间

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

7.开启gzip压缩

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

8.访问日志

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

9.非HTTP跳转https

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













