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



## 常见问题
1.访问日志中有大量的head请求，处理方式
```nginx
server{
	if ($request_method ~ ^(HEAD)$ ) {
		return 200 "All OK";
	}
}
```













