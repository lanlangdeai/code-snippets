# js常用函数



## 时间

```js
// 获取当前时间戳
function nowTimestamp()
{
	return Date.parse(new Date)/1000;
}

// 获取当前时间 
function now()
{
    var myDate = new Date();

    var year  = myDate.getFullYear();//获取当前年
    var month = myDate.getMonth()+1; //获取当前月
    var date  = myDate.getDate();    //获取当前日
    var h = myDate.getHours();       //获取当前小时数(0-23)
    var m = myDate.getMinutes();     //获取当前分钟数(0-59)
    var s = myDate.getSeconds();     //获取当前秒数(0-59)

    return year+'-'+p(month)+"-"+p(date)+" "+p(h)+':'+p(m)+":"+p(s);
}
function p(s) {
    return s < 10 ? '0' + s: s;
}

// 将日期转化成时间戳	 2014-01-01 20:20:20	
function datetimeToUnix(datetime)
{
	var f = datetime.split(' ', 2);
    var d = (f[0] ? f[0] : '').split('-', 3);
    var t = (f[1] ? f[1] : '').split(':', 3);
    return (new Date(
            parseInt(d[0], 10) || null,
            (parseInt(d[1], 10) || 1) - 1,
            parseInt(d[2], 10) || null,
            parseInt(t[0], 10) || null,
            parseInt(t[1], 10) || null,
            parseInt(t[2], 10) || null
            )).getTime() / 1000;
}

// 将时间戳转化成便于阅读的时间格式 
function unixToDatetime(unixTime, isFull, timeZone)
{
	if (typeof (timeZone) == 'number')
    {
        unixTime = parseInt(unixTime) + parseInt(timeZone) * 60 * 60;
    }
    var time = new Date(unixTime * 1000);
    var ymdhis = "";
    ymdhis += time.getUTCFullYear() + "-";
    ymdhis += (time.getUTCMonth()+1) + "-";
    ymdhis += time.getUTCDate();
    if (isFull === true)
    {
        ymdhis += " " + time.getUTCHours() + ":";
        ymdhis += time.getUTCMinutes() + ":";
        ymdhis += time.getUTCSeconds();
    }
    return ymdhis;
}
```

