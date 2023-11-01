# MongoDB


## 常用脚本

1. 管理MongoDB操作脚本
```bash
start() 
{
    /usr/bin/mongod --fork --config /etc/mongod.conf 
}
 
stop() 
{
   /usr/bin/mongod --config /etc/mongod.conf --shutdown
}
 
case "$1" in
start)
    start
    ;;
 
stop)
    stop
    ;;
 
restart)
    stop
    start
    ;;
 
*)
    echo "Usage: $0 {start|stop|restart}"
    exit 0
    ;;
 
esac
exit 0
```