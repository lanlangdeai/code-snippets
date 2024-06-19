# PHP常用方法&函数



## 字符

#### 生成手机验证码

```php
//方法一:
function randString($len=6)
{
    $chars = str_repeat('0123456789', 3);
    // 位数过长重复字符串一定次数
    $chars = str_repeat($chars, $len);
    $chars = str_shuffle($chars);
    $str = substr($chars, 0, $len);
    return $str;
}

//方法二:
function randomKeys($length=6)
{
    $key='';
    $pattern='1234567890';
    for($i=0;$i<$length;++$i)
    {
        $key .= $pattern{mt_rand(0,9)};
    }
    return $key;
}

//方法三:
function randomCaptcha(){
    $randNumber=mt_rand(100000,999999);
    str_shuffle($randNumber);
    return $randNumber;
}
```









## URl

#### 链接跳转

```php
/**
 * URL地址跳转
 * @param $url 跳转地址
 * @param int $time 跳转间隔
 * @param string $msg 显示信息
 */
function redirect($url, $time = 0, $msg = '')
{
    $url = str_replace(array("\n", "\r"), '', $url);
    if (empty($msg))
        $msg = "系统将在{$time}秒之后自动跳转到{$url}！";
    //没有发送header头之前进行设置
    if (!headers_sent()) {
        if (0 === $time) {
            header('Location: ' . $url);
        } else {
            header("refresh:{$time};url={$url}");
            echo($msg);
        }
        exit();
    } else {
        $str = "<meta http-equiv='Refresh' content='{$time};URL={$url}'>";
        if ($time != 0)
            $str .= $msg;
        exit($str);
    }
}
```

#### 拼接URL地址

```php
/**
 * 拼接URL地址
 * @param string $url 地址
 * @param array $params 参数
 * @return string 完整参数地址
 */
function generateUrl($url, array $params = [])
{
    if(!$params) return $url;

    if(strpos($url, '?') === false){
        return $url .'?'. http_build_query($params, null, '&');
    }

    list($path, $query_string) = explode('?', $url, 2);
    $query_array = [];
    parse_url($query_string, $query_array);
    $params = array_merge($params, $query_array);
    return $path .'?'. http_build_query($params, null, '&');
}
```



## IP

#### 获取客户端ip地址

```php
//获取ip(1)
function getClientIP()
{
    if (isset($_SERVER)) {
        if (isset($_SERVER["HTTP_X_FORWARDED_FOR"])) {
            $realip = $_SERVER["HTTP_X_FORWARDED_FOR"];
        } else
            if (isset($_SERVER["HTTP_CLIENT_IP"])) {
                $realip = $_SERVER["HTTP_CLIENT_IP"];
            } else {
                $realip = $_SERVER["REMOTE_ADDR"];
            }
    } else {
        if (getenv("HTTP_X_FORWARDED_FOR")) {
            $realip = getenv("HTTP_X_FORWARDED_FOR");
        } else
            if (getenv("HTTP_CLIENT_IP")) {
                $realip = getenv("HTTP_CLIENT_IP");
            } else {
                $realip = getenv("REMOTE_ADDR");
            }
    }

    return addslashes($realip);
}


//获取ip(2)
function getClientIp2()
{
    $ip = 'unknown';
    $unknown = 'unknown';

    if (isset($_SERVER['HTTP_X_FORWARDED_FOR']) && $_SERVER['HTTP_X_FORWARDED_FOR'] && strcasecmp($_SERVER['HTTP_X_FORWARDED_FOR'], $unknown)) {
        // 使用透明代理、欺骗性代理的情况
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];

    } elseif (isset($_SERVER['REMOTE_ADDR']) && $_SERVER['REMOTE_ADDR'] && strcasecmp($_SERVER['REMOTE_ADDR'], $unknown)) {
        // 没有代理、使用普通匿名代理和高匿代理的情况
        $ip = $_SERVER['REMOTE_ADDR'];
    }

    // 处理多层代理的情况
    if (strpos($ip, ',') !== false) {
        // 输出第一个IP
        $ip = reset(explode(',', $ip));
    }

    return $ip;
}


//获取IP(3)
function getClientIp3()
{
    foreach (array('HTTP_CLIENT_IP', 'HTTP_X_FORWARDED_FOR', 'HTTP_X_FORWARDED', 'HTTP_X_CLUSTER_CLIENT_IP', 'HTTP_FORWARDED_FOR', 'HTTP_FORWARDED', 'REMOTE_ADDR') as $key)
    {
        if (array_key_exists($key, $_SERVER) === true)
        {
            foreach (explode(',', $_SERVER[$key]) as $ip)
            {
                $ip = trim($ip);

                if (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE) !== false)
                {
                    return $ip;
                }
            }
        }
    }
}
```





## 校验

#### Ip校验

```php
function ip( $str )
{
    if ( empty( $str ) )
        return false;

    if ( !preg_match( '/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/', $str ) ) {
        return false;
    }

    $ip_array = explode( '.', $str );

    //真实的ip地址每个数字不能大于255（0-255）
    return ( $ip_array[0] <= 255 && $ip_array[1] <= 255 && $ip_array[2] <= 255 && $ip_array[3] <= 255 ) ? true : false;
}
```











