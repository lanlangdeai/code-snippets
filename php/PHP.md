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



## 常用操作

### 项目中错误展示与级别设置

```php
$project_environment = getenv('PROJECT_ENVIRONMENT');
if($project_environment == 'production'){
    defined('PRO_ENV') or define('PRO_ENV', 'prod');
}elseif($project_environment == 'test'){
    defined('PRO_ENV') or define('PRO_ENV', 'test');
    ini_set('display_errors', 1);
    //开启错误和警告，严格规范开发
    error_reporting(E_ALL ^E_NOTICE);
}else{
    defined('PRO_ENV') or define('PRO_ENV', 'dev');
    ini_set('display_errors', 1);
    //开启错误和警告，严格规范开发
    error_reporting(E_ALL ^E_NOTICE);
}
```



### 跨域处理

```php
// 设置允许其他域名访问
header('Access-Control-Allow-Origin:*');  
// 设置允许的响应类型 
header('Access-Control-Allow-Methods:POST, GET');  
// 设置允许的响应头 
header('Access-Control-Allow-Headers:x-requested-with,content-type'); 


$origin = isset($_SERVER['HTTP_ORIGIN'])? $_SERVER['HTTP_ORIGIN'] : '';
$allow_origin = array(
    'http://domain1',
    'http://domain2',
    'https://domain3',
);
if(in_array($origin, $allow_origin)){
    header('Access-Control-Allow-Origin:'.$origin);
    header('Access-Control-Allow-Methods:POST,GET');
    header('Access-Control-Allow-Headers:x-requested-with,content-type');
}
```

