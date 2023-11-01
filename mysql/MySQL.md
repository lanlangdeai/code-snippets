# MySQL



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






## 常见问题

1. ### MySQL数据导入报错：Got a packet bigger than‘max_allowed_packet’bytes的问题

解决： 修改my.cnf配置， 然后重启MySQL

```
添加配置项：
max_allower_package=512M
```