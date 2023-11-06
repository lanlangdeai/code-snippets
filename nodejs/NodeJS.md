# NodeJS



## 安装
[Yum]

```bash
yum install centos-release-scl-rh
yum-config-manager --enable rhel-server-rhscl-7-rpms
yum install rh-nodejs12
scl enable rh-nodejs12 bash
```
说明：如果想安装其他的版本的Node， 直接替换后面的版本号即可


## NPM
[Node.js](https://nodejs.org/) 的依赖包管理生态系统 [npm](https://www.npmjs.com/), 是世界上最大的生态系统开源库。

### npm 加速
1. 在安装软件的时候使用--registry来注册镜像地址到国内的镜像（每次使用都需要指定国内的镜像）
```
npm install gitbook-cli -g --registry=http://registry.npm.taobao.org
```

2. 可以将国内镜像设置为默认的镜像源
```
npm config set registry=http://registry.npm.taobao.org
```

3. 使用cnpm来替代npm
```bash
npm install -g cnpm --registry=https://registry.npm.taobao.org
# 安装完成之后就可以使用cnpm来进行相关软件的安装
cnpm install  [name]
```

