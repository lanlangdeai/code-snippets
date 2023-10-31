# nginx



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
