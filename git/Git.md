# Git

## 安装

```shell

yum install -y curl-devel expat-devel gettext-devel \
  openssl-devel zlib-devel

yum -y install git-core
# 查看版本
git --version
git version 1.8.3.1
```



## 常用命令

```shell
# 生成秘钥对
ssh-keygen -t rsa -C "你的邮箱@xxx.com"

# 将公钥推送到远端(实现免密登录)
## Linux
ssh-copy-id -i .ssh/id_rsa.pub  用户名字@192.168.x.xxx
## Windows
cat .\id_rsa.pub | ssh root@122.51.15.110 "cat >> ~/.ssh/authorized_keys"
```





## 相关文件

.gitignore 是放置一些不想添加到版本库中的文件或者目录

例如：标识忽略该目录下所有文件但不包含.gitignore文件

```
*
!.gitignore
```



.gitkeep 占位文件
在git中如果是一个空的文件夹是不允许被提交的，所有可以添加一个.gitkeep的文件作为一个占位符，这样的话这个空文件就可以被提交到版本库中了







