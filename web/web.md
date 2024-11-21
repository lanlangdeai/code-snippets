# Web前端



## 示例

1. 发起get请求

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

```

2. 事件监听

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

3. 获取请求参数

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

4. 生成二维码

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

5. 微信相关

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

// 3. 
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
```

6. 验证相关

```js
// 是否是iOS
var isiOS = !!navigator.userAgent.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/);


```

7. 浏览器信息

```js
// ua
var ua = navigator.userAgent.toLowerCase();


```





## 常见问题

缓存处理方案:

1).页面不缓存

```html
<META HTTP-EQUIV="pragma" CONTENT="no-cache"> 
<META HTTP-EQUIV="Cache-Control" CONTENT="no-cache, must-revalidate"> 
<META HTTP-EQUIV="expires" CONTENT="0">
```

2)随机数或时间戳

```html
// 在 URL 参数后加上 "?timestamp=" + new Date().getTime(); 
```

3)后台设置

```php
header("Cache-Control: no-cache, must-revalidate");
```

4)replace跳转覆盖

```js
window.location.replace("WebForm1.aspx");
```

