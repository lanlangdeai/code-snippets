# PostgreSQL

## 安装

```bash
#1 根据系统选择rpm
https://www.postgresql.org/download/linux/redhat/

#2 创建安装脚本并运行
vim postgresql11.sh

#将上一步的script拷贝到文件中
bash postgresql11.sh

#3 设置postgres用户密码
passwd postgres

#4 配置postgresql11
cd /var/lib/pgsql/ data
vim postgresql.conf

#5 运行postgres客户端
sudo -u postgres psql -U postgres

#6 安装postgres开发包
yum install postgresql-devel
```

