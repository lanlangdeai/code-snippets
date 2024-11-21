# Web前端



## 示例

1. 发起get请求

```js
<script type="text/javascript">
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
</script>
```

2. 事件监听

```js
// 页面加载后执行
window.addEventListener('pageshow', function (e) {
        todo();
});
```

3. 获取请求参数

```js
function getParam(){
            var res = location.search.substring(1).split('&');

            var items = {};
            for(var i=0;i<res.length;i++){
                var a = res[i].split('=');
                items[a[0]] = a[1];
            }
            return items
        }
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

