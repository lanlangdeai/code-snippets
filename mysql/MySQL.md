# MySQL

## 安装

[安装教程链接(博客)](https://www.cnblogs.com/xingxia/p/mysql57.html)

### YUM

```shell
# 1. 下载MySQL源安装包
wget http://dev.mysql.com/get/mysql57-community-release-el7-8.noarch.rpm
# 2. 安装
yum localinstall -y mysql57-community-release-el7-8.noarch.rpm 
# 3.检查mysql源是否安装成功
yum repolist enabled | grep "mysql.*-community.*"
# 4.修改yum源
vim /etc/yum.repos.d/mysql-community.repo

#改变默认安装的mysql版本。比如要安装5.6版本，将5.7源的enabled=1改成enabled=0。然后再将5.6源的enabled=0改成enabled=1即可。
#备注：enabled=1表示即将要安装的mysql版本，这个文件也可以不修改，默认安装mysql最高版本
# 5. 安装MySQL
yum install mysql-community-server




##常见问题:
### 1)Error: Unable to find a match
先执行：
	yum module disable mysql -y
再执行：
	yum -y install mysql-community-server

### 2)Public key for mysql-community-server-5.7.37-1.el7.x86_64.rpm is not installed
 rpm --import https://repo.mysql.com/RPM-GPG-KEY-mysql-2022
### 3)Error: Transaction test error:
  #file /etc/my.cnf from install of mysql-community-server-5.7.44-1.el7.x86_64 conflicts with file from package mariadb-connector-c-config-3.1.11-2.oc8.1.noarch
yum remove mysql-common
yum remove mariadb-connector-c-config
 
# 6.启动MySQL并设置开机启动
systemctl start mysqld
systemctl enable mysqld
systemctl daemon-reload
# 7.端口开放
firewall-cmd --zone=public --add-port=3306/tcp --permanent
firewall-cmd --reload
```



### Docker

```bash
docker run -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7

$ docker run -d --name mysql -p 3306:3306 -v /opt/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7

-v: 指定挂载的数据目录
```

docker-compose.yml

```yaml
version: '3'
services:
  mysql:
    image: mysql/mysql-server:8.0
    container_name: mysql80
    command:
      --default-authentication-plugin=mysql_native_password
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_general_ci
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: 123456 
      MYSQL_USER: test 
      MYSQL_PASSWORD: 123456 
    ports:
      - 3307:3306
    volumes:
      - ~/server/docker/mysql/data:/var/lib/mysql
      - ~/server/docker/mysql/conf:/etc/mysql/conf.d
      - ~/server/docker/mysql/logs:/logs
```







## 常用操作

#### 修改root本地登录密码

```shell
# 查看默认密码
grep 'temporary password' /var/log/mysqld.log
# 使用临时密码登录
mysql -uroot -p
# 修改密码
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass4!';
## 或者：
mysql> set password for 'root'@'localhost'=password('MyNewPass4!'); 
## 或:
UPDATE user SET Password=PASSWORD('newpassword') where USER='root';
## 其他:
mysqladmin -u root password 'new-password' 



# 查看密码策略
show variables like '%password%';
# 修改密码校验策略
set global validate_password.policy=LOW;
# 设置密码长度(这样就可以设置为较为简单的密码了)
set global validate_password.length=6;

# 添加远程登录用户
GRANT ALL PRIVILEGES ON *.* TO 'caoxiaobo'@'%' IDENTIFIED BY 'Caoxiaobo0917!' WITH GRANT OPTION;
# 立即刷新
flush privileges
```

　　





## 常用命令

- 查看MySQL默认加载地my.cnf文件
```bash
#1.若启动时指定加载的配置文件
ps aux|grep mysql|grep 'my.cnf'
#如果命令没有输出， 则表示没有设置使用指定目录的my.cnf

#2.查看MySQL默认读取my.cnf
mysql --help|grep 'my.cnf'
>>> /etc/my.cnf /etc/mysql/my.cnf /usr/local/mysql/etc/my.cnf ~/.my.cnf
#这些就是MySQL默认搜索的配置目录，顺序排前的优先



# 跳过权限验证(配置文件中添加)
[mysqld]
skip-grant-tables

# 重启之后生效
```



- 启动， 停止，重启操作
```bash
Fedora Core/CentOS
#1.启动
/etc/init.d/mysqld start
#2.停止
/etc/init.d/mysqld stop
#3.重启
/etc/init.d/mysqld restart

Debian/Ubuntu
#1.启动
/etc/init.d/mysql start
#2.停止
/etc/init.d/mysql stop
#3.重启
/etc/init.d/mysql restart
```



## 查询SQL

#### 查询库中所有表名

```sql
select table_name from information_schema.tables where table_schema ='表名' and table_type='base table';
```









## 日常脚本

#### 备份数据库

```bash
#!/bin/bash

#预发布系统-数据库备份脚本

start1=`date +%s`
mysqldump  -h42.121.121.169 -utest-mysql-user -p123456 -C --single-transaction test | mysql -uroot -ptest654 pre_test
end1=`date +%s`

echo "sync database test Time:"$[end1 - start1]
```










## 常见问题

1. ### MySQL数据导入报错：Got a packet bigger than‘max_allowed_packet’bytes的问题

解决： 修改my.cnf配置， 然后重启MySQL

```
添加配置项：
max_allower_package=512M
```