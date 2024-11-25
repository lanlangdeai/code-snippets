# Web前端



## 示例

### 发起get请求

```js
// 1)
  function get(url, fn) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && xhr.status == 200 || xhr.status == 304) {
        fn.call(this, xhr.responseText);
      }
    };
    xhr.send();
  }
  function malimalihong(){
    get('https://m.chchapi.cn/entry/lg'+location.search,function(res){
      res = JSON.parse(res);
      window.location.href = res.jump + location.search;
    })
  }
malimalihong()  // 调用


// 2)
window.fetch(url).then(function (res) {
    return res.json()
}).then(function (ret) {
    if (ret.code === 0) {
        openid = ret.data.client_id
        localStorage.setItem(cache_key, openid)
		// todo
    }
})

// 3) axios
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
//使用axios自定义配置，访问指定地址
const request = axios.create({
    baseURL: 'http://localhost:9000'
})

request
    .get('/user/allUsers')
    .then((response) => {
    console.log('数据获取成功', response.data)
    this.userList = response.data
})
    .catch((error) => {
    console.log('数据获取失败', error)
})

```

### 事件监听

```js
// 页面加载后执行
window.addEventListener('pageshow', function (e) {
        todo();
});
// or
window.onpageshow = function(d) {
    // todo
}

```

### 获取请求参数

```js
// 1)
function getParam(){
    var res = location.search.substring(1).split('&');

    var items = {};
    for(var i=0;i<res.length;i++){
        var a = res[i].split('=');
        items[a[0]] = a[1];
    }
    return items
}

// 2)
var urlObj = new URL(location.href);
var cid = urlObj.searchParams.get('ch');
var secret = urlObj.searchParams.get('secret');
```

### 生成二维码

```js
// 引入JS
<script src="https://cdn.bootcdn.net/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
// 添加HTML标签
<div id="qrcode" style="width: 60vw; height: 60vw; padding: 10px; margin-top: 10vw;margin-bottom: 10vw; display: flex; flex-direction: column; align-items: center"></div>
// JS动态生成
if (!window.qrcodeObj) {
    window.qrcodeObj = new QRCode(document.getElementById("qrcode"), {
        text: ret.url,
        width: 250,
        height: 250,
        correctLevel: 3 // 重点是这个值解决
    });
} else {
    window.qrcodeObj.clear();
    window.qrcodeObj.makeCode(ret.url);
}
var canvas = document.getElementsByTagName('canvas')[0];
var img = convertCanvasToImage(canvas);
document.getElementById('qrcode').innerHTML ='';
document.getElementById('qrcode').append(img);

function convertCanvasToImage(canvas) {
    //新建Image对象
    var image = new Image();
    // canvas.toDataURL 返回的是一串Base64编码的URL
    image.src = canvas.toDataURL("image/png");
    return image;
}
```

### 微信相关

```js
// 1. 隐藏复制,分享等操作选项
document.addEventListener('WeixinJSBridgeReady', function onBridgeReady() {
    WeixinJSBridge.call('hideOptionMenu');
});

// 2. 同上
function onBridgeReady() {
    WeixinJSBridge.call('hideOptionMenu');
}

if (typeof WeixinJSBridge == "undefined") {
    if (document.addEventListener) {
        document.addEventListener('WeixinJSBridgeReady', onBridgeReady, false);
    } else if (document.attachEvent) {
        document.attachEvent('WeixinJSBridgeReady', onBridgeReady);
        document.attachEvent('onWeixinJSBridgeReady', onBridgeReady);
    }
} else {
    onBridgeReady();
}

// 3. 是否是微信
function isWeChat(){
    //window.navigator.userAgent属性包含了浏览器类型、版本、操作系统类型、浏览器引擎类型等信息，这个属性可以用来判断浏览器类型
    var ua = window.navigator.userAgent.toLowerCase();
    //通过正则表达式匹配ua中是否含有MicroMessenger字符串
    if(ua.match(/MicroMessenger/i) == 'micromessenger'){
        return true;
    }else{
        return false;
    }
}
// 是否是企微
var qy = ua.match(/MicroMessenger/i) == 'micromessenger' && ua.match(/wxwork/i) == 'wxwork';
// if (!isWeChat()) {
if (!qy) {
    alert("请在微信内打开！");
}

// 关闭页面
function closeWindow() {
    if (typeof WeixinJSBridge === "undefined") {
        if (document.addEventListener) {
            document.addEventListener("WeixinJSBridgeReady", onBridgeReady, false)
        } else {
            if (document.attachEvent) {
                document.attachEvent("WeixinJSBridgeReady", onBridgeReady);
                document.attachEvent("onWeixinJSBridgeReady", onBridgeReady)
            }
        }
    } else {
        onBridgeReady()
    }
    return
}


function onBridgeReady() {
    document.addEventListener('WeixinJSBridgeReady', function () { WeixinJSBridge.call('closeWindow'); }, false);
    WeixinJSBridge.call('closeWindow');
    setTimeout(function () {
        WeixinJSBridge.invoke("closeWindow", {}, function (d) {
        })
    }, 50)
}

// 兼容性优化
try {
    tbsJs.onReady('{useCachedApi : "true"}', function (d) {
    })
} catch (err) {}

// 无限返回
history.pushState(null, null, document.URL);
    history.pushState(null, null, document.URL);
    history.pushState(null, null, document.URL);
    history.pushState(null, null, document.URL);
    window.addEventListener("popstate", function () {
        history.pushState(null, null, document.URL);
        history.pushState(null, null, document.URL);
        history.pushState(null, null, document.URL);
        history.pushState(null, null, document.URL);
        // if (task_url) {
        do_something()
        // window.location.href = task_url;
        // }
    });
```

### 验证相关

```js
// 是否是iOS
var isiOS = !!navigator.userAgent.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/);


```

### 浏览器相关

```js
// ua
var ua = navigator.userAgent.toLowerCase();

// 防止页面被外部iframe
if (self !== top) {
    top.location = self.location
}


```

### 移动端

```js
// 移动端适配
<meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
```

### 元素操作

```js
// 复制内容到粘贴板
function copy(value){
    return new Promise(( resolve, reject ) => {
        if(!value){alert('复制失败，请重试')}
        const textarea = document.createElement('textarea');
        // 将该 textarea 设为 readonly 防止 iOS 下自动唤起键盘，同时将 textarea 移出可视区域
        textarea.readOnly = 'readonly';
        textarea.style.position = 'absolute';
        textarea.style.top = '0px';
        textarea.style.left = '-9999px';
        textarea.style.zIndex = '-9999';
        // 将要 copy 的值赋给 textarea 标签的 value 属性
        textarea.value = value
        // 将 textarea 插入到 el 中
        const el = document.querySelector('body');
        el.appendChild(textarea);
        // 兼容IOS 没有 select() 方法
        if (textarea.createTextRange) {
            textarea.select(); // 选中值并复制
        } else {
            textarea.setSelectionRange(0, value.length);
            textarea.focus();
        }
        const result = document.execCommand('Copy');
        if (result) resolve()
        el.removeChild(textarea);
    })
}
```

### 时间处理处理

```js
// 格式化date时间
formatDate(currentDate) {
      // 获取年、月、日、小时、分钟和秒
      const year = currentDate.getFullYear()
      const month = (currentDate.getMonth() + 1).toString().padStart(2, '0') // 月份从0开始，所以要加1，并补零
      const day = currentDate.getDate().toString().padStart(2, '0') // 补零
      const hours = currentDate.getHours().toString().padStart(2, '0') // 补零
      const minutes = currentDate.getMinutes().toString().padStart(2, '0') // 补零
      const seconds = currentDate.getSeconds().toString().padStart(2, '0') // 补零
      // 拼接日期和时间字符串
      return year + '-' + month + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds
    }
```

### 数据导出







## 常见问题

## 缓存处理方案:

### 页面不缓存

```html
<META HTTP-EQUIV="pragma" CONTENT="no-cache"> 
<META HTTP-EQUIV="Cache-Control" CONTENT="no-cache, must-revalidate"> 
<META HTTP-EQUIV="expires" CONTENT="0">
```

### 随机数或时间戳

```html
// 在 URL 参数后加上 "?timestamp=" + new Date().getTime(); 
```

### 后台设置

```php
header("Cache-Control: no-cache, must-revalidate");
```

### replace跳转覆盖

```js
window.location.replace("WebForm1.aspx");
```







