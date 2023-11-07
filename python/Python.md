# Python


## 相关文档

- 官方文档: [https://docs.python.org/3/](https://docs.python.org/3/)
- 官网中文版3.7: [https://docs.python.org/zh-cn/3.7/download.html](https://docs.python.org/zh-cn/3.7/download.html)



## 安装

1.安装依赖包
```bash
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

2.下载python源码包到指定目录
```bash
cd /usr/local/src
wget https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz

#其他版本：
#37)
wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz
#39)
wget https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz

```

3.创建安装目录并安装
```bash
mkdir -p /usr/local/python3

# 解压
tar -zxvf Python-3.8.12.tgz

# 安装编译器gcc
yum install gcc

# 安装libffi-devel(3.7版本之后需要的包)
yum install libffi-devel -y

cd Python-3.8.12
.configure --prefix=/usr/local/python3
make && make install
```

4.检查是否安装成功
```bash
/usr/local/python3/bin/python3 -V
```

5.建立python软链接
```bash
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3  /usr/bin/pip3
```

6.添加环境变量
```bash
vim /etc/profile

最后添加代码
export PATH=$PATH:$HOME/bin:/usr/local/python3/bin

# 立即生效
source /etc/profile
```

## Pip加速
1.临时使用

```bash
pip install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple
```

2.永久设置

```bash
# 清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 阿里源
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
# 腾讯源
pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple
# 豆瓣源
pip config set global.index-url http://pypi.douban.com/simple/
```



## 常用第三方包
- [fake-useragent](./package.md) (代理伪造，随机生成UA)
- [loguru]([https://github.com/Delgan/loguru](https://github.com/Delgan/loguru) (日志记录器)





## 基础
```python

# 数据类型
## 字符串
'''
1.索引切片 [开始索引:结束索引:步长]   顾头不顾尾
[:3]       0到3
[2:]       2到最后一位
[1:8:2]    从1到8,隔一个取一个值
[:]        复制整个内容
[::-1]     字符串反转


## 浮点型

## 布尔值
True | False


## 元祖


## 列表

## 字典

## None



'''










```






















## 方法&函数




