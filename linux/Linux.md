# Linux 



## 软件包

### Zip

```shell
#1. 安装
## Centos
yum install -y zip
## Ubuntu
apt-get install zip

#2. 使用
 1) 将所有内容添加到test.zip压缩文件
    zip  -r  test.zip  ./*   
     
 2）解压zip文件到当前目录
    unzip test.zip

 3) 解压zip到指定目录并覆盖
    unzip -o -d /home/test   test.zip 
     
    	-o: 不提示的情况下覆盖文件
        -d:  指定文件解压缩到/home/test目录下

```



### [Rar](https://www.rarlab.com)

```shell
# 安装 
## 源码安装
wget https://www.rarlab.com/rar/rarlinux-x64-5.9.1.tar.gz
tar  -zxvf  rarlinux-x64-5.9.1.tar.gz 
cd rar
make

## yum安装
yum install -y rar
yum install -y unrar


# 使用
1)添加目录为压缩文件
rar a test.rar test
	a: Add files to archive

2)解压缩文件
rar x test.rar
	x: 解压缩

unrar e test.rar



```











## 常用命令

1.判断文件或目录是否存在， 不存在则创建
```bash
#文件：
test -f test.txt || touch test.txt

#目录：
test -d /opt/scripts || mkdir -p /opt/scripts

```


## 脚本汇总









