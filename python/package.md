# 第三方包

## fake-useragent (代理伪造，随机生成UA)

安装：
```bash
pip install fake-useragent
```

使用：
```python
from fake_useragent import UserAgent

ua = UserAgent()
#ie浏览器的user agent
print(ua.ie)

#opera浏览器
print(ua.opera)

#chrome浏览器
print(ua.chrome)

#firefox浏览器
print(ua.firefox)

#safri浏览器
print(ua.safari)

#最常用的方式
#写爬虫最实用的是可以随意变换headers，一定要有随机性。支持随机生成请求头
print(ua.random)
print(ua.random)
print(ua.random)
```



## loguru(日志记录器)([https://github.com/Delgan/loguru](https://github.com/Delgan/loguru)

安装：
```
pip install loguru
```


使用：
```python
from loguru import logger

# 输出到控制台
logger.debug('this is a debug')

# 追加到文件
logger.add("file_{time}.log")
logger.debug("this is a debug for log")

# 日志时间滚动
logger.add("file_2.log", rotation="12:00")  # 每天12:00会创建一个新的文件
logger.debug('this a rotation debug for log')
过了设定的时间，则将原来的 file_2.log 重命名，并添加一个新的 file_2.log 文件

#日志大小滚动
logger.add("file_1.log", rotation="1 MB")
logger.debug('this is a size debug for log')

#如果你不想删除原有日志文件，Loguru 还支持将日志直接压缩：
logger.add("file_Y.log", compression="zip")    # 压缩日志

#自定义颜色
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

#多进程安全
#Loguru 默认情况下是线程安全的，但它不是多进程安全的。不过如果你需要多进程/异步记录日志，它也能支持，只需要添加一个 enqueue 参数：
logger.add("somefile.log", enqueue=True)

#支持traceback
logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)
```
