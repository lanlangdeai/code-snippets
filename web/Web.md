# Web前端



## 示例

1. 发起get请求

```js
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

