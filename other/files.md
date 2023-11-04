# 文件相关

## .htaccess

.htaccess是一个纯文本文件，它里面存放着Apache服务器配置相关的指令。
.htaccess主要的作用有：URL重写、自定义错误页面、MIME类型配置以及访问权限控制等。主要体现在伪静态的应用、图片防盗链、自定义404错误页面、阻止/允许特定IP/IP段、目录浏览与主页、禁止访问指定文件类型、文件密码保护等。
.htaccess的用途范围主要针对当前目录。

启用.htaccess，需要修改httpd.conf，启用AllowOverride，并可以用AllowOverride限制特定命令的使用。
打开httpd.conf文件用文本编辑器打开后,查找 

```
<Directory />
    Options FollowSymLinks
    AllowOverride None
</Directory>

改为：

<Directory />
    Options FollowSymLinks
    AllowOverride All
</Directory>
```

示例：

```
1.阻止所有人访问该目录
deny from all
```



## .gitignore 





## robots.txt


