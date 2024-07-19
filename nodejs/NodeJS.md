# NodeJS



## 安装
[Linux]

```shell
#nvm
# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# download and install Node.js (you may need to restart the terminal)
nvm install 12

# verifies the right Node.js version is in the environment
node -v # should print `v12.22.12`

# verifies the right NPM version is in the environment
npm -v # should print `6.14.16`


设置npm_mirror:
nvm npm_mirror https://npmmirror.com/mirrors/npm/
设置node_mirror:
nvm node_mirror https://npmmirror.com/mirrors/node/

```




[Windows]

```shell
# installs fnm (Fast Node Manager)
winget install Schniz.fnm

# download and install Node.js
fnm use --install-if-missing 22

# verifies the right Node.js version is in the environment
node -v # should print `v22.3.0`

# verifies the right NPM version is in the environment
npm -v # should print `10.8.1`

# 临时
在一个新的终端中需要执行命令才可以正常使用 fnm env --use-on-cd | Out-String | Invoke-Expression
# 永久
1.在powershell中需要新建文件 %USERPROFILE%\Documents\WindowsPowerShell\profile.ps1
# %USERPROFILE%: 表示用户目录，直接在文件管理的地址栏输入 %USERPROFILE%，然后回车
2.文件中写入命令
fnm env --use-on-cd | Out-String | Invoke-Expression

# 更多其他终端的设置: https://juejin.cn/post/7113462239734022158


```





## 使用

- 使用命令

  ```shell
  # 查看node版本
  node -v
  # 执行脚本
  node server.js
  # 执行一段代码
  node -e 'const name="lanlang";console.log(name)'
  # 以调试模式启动并且在首行断住
  node --inspect-brk ./debug.js
  # 调试模式运行
  node inspect debug-inspect.js
  
  
  # 查看npm版本
  npm -v
  # 升级
  npm install npm@latest -g
  # 清理缓存
  npm cache clean
  ```
  
  

![node_inspect](E:\lanlang\code-snippets\nodejs\images\node_inspect.png)








## NPM
[Node.js](https://nodejs.org/) 的依赖包管理生态系统 [npm](https://www.npmjs.com/), 是世界上最大的生态系统开源库。

### npm 加速
1. 在安装软件的时候使用--registry来注册镜像地址到国内的镜像（每次使用都需要指定国内的镜像）
```shell
npm install gitbook-cli -g --registry=http://registry.npm.taobao.org
```

2. 可以将国内镜像设置为默认的镜像源
```shell
npm config set registry=http://registry.npm.taobao.org
```

3. 使用cnpm来替代npm
```shell
npm install -g cnpm --registry=https://registry.npm.taobao.org
# 安装完成之后就可以使用cnpm来进行相关软件的安装
cnpm install  [name]
```





## 第三方

[orm](https://www.npmjs.com/package/orm)

对象关系映射





[fnm](https://juejin.cn/post/7113462239734022158): 多版本工具(更多还有nvm, n)

```shell
# 查看使用命令
fnm -h

# 安装指定版本nodejs
fnm install 18/16/14/12

# 使用某个版本
fnm use 18

# 设置默认使用版本
fnm default 18
```

