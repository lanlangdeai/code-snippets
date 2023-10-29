# PHP


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

