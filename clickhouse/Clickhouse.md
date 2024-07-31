# Clickhouse



## 安装

### Yum

```bash
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://packages.clickhouse.com/rpm/clickhouse.repo
sudo yum install -y clickhouse-server clickhouse-client

sudo /etc/init.d/clickhouse-server start
clickhouse-client # or "clickhouse-client --password" if you set up a password.
```



## 启动服务

```bash
/etc/init.d/clickhouse-server start

#手动启动:
clickhouse-server --config-file=/etc/clickhouse-server/config.xml


#日志文件将输出在/var/log/clickhouse-server/文件夹。
#检查/etc/clickhouse-server/config.xml中的配置。
```



## 客户端命令

```bash
#指定端口连接
clickhouse-client --port 9020 
```



## 配置

```bash
#ClickHouse安装后，默认client连接端口是9000
#默认配置文件是只读, 首先需要修改配置文件权限:
chmod u+w /etc/clickhouse-server/config.xml

<tcp_port>9020</tcp_port>
#tcp_port 端口进行修改
    

#远程连接:
#找到<listen_host>::</listen_host>的配置项，取消注释，这样就同时支持IPv4和IPv6了。
#也可以选择取消注释<listen_host>0.0.0.0</listen_host>，就仅支持IPv4，不允许IPv6。
```

















