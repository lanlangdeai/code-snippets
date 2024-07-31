# PHP

## 安装







## 常用命令

```shell
# 查看PHP加载的配置文件
php -i|grep php.ini

# 查看php cli加载的配置文件
php --ini

# 查看加载的php扩展目录
php -i|grep extension_dir

# 平滑重启php-fpm
kill -USR2 16550
or
kill -USR2 `cat /usr/local/var/run/php-fpm.pid`
# USR2 平滑重启所有worker进程并重新载入配置和二进制模块


```


















## Composer 

### 镜像加速

```bash
# 取消全局配置
composer config -g --unset repos.packagist

# 全局设置
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/

# 单独设置
composer config repo.packagist composer https://mirrors.aliyun.com/composer/


## 更多设置
# 腾讯云
composer config -g repos.packagist composer https://mirrors.cloud.tencent.com/composer/



```
### 安装依赖包
```bash
# 存在composer.json文件的情况
composer install

# 安装单独包
composer require 包名称

```

