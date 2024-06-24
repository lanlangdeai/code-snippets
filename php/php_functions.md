# PHP常用方法&函数

- 检测设备(手机,PC,iOS等): https://github.com/serbanghita/Mobile-Detect
- 















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



## 字符串

#### 字符串截取

```php

/**
 * 字符串截取，支持中文和其它编码
 * @param string $str 需要转换的字符串
 * @param int $start 开始位置
 * @param int $length 截取长度
 * @param string $charset 编码格式
 * @param boolean $suffix 截断显示字符
 * @return false|string
 */
function msubstr($str, $start, $length, $charset = "utf-8", $suffix = true)
{
    if (function_exists("mb_substr")){
        return mb_substr($str, $start, $length, $charset);
    }
    elseif (function_exists('iconv_substr')) {
        return iconv_substr($str, $start, $length, $charset);
    }
    $re['utf-8'] = "/[\x01-\x7f]|[\xc2-\xdf][\x80-\xbf]|[\xe0-\xef][\x80-\xbf]{2}|[\xf0-\xff][\x80-\xbf]{3}/";
    $re['gb2312'] = "/[\x01-\x7f]|[\xb0-\xf7][\xa0-\xfe]/";
    $re['gbk'] = "/[\x01-\x7f]|[\x81-\xfe][\x40-\xfe]/";
    $re['big5'] = "/[\x01-\x7f]|[\x81-\xfe]([\x40-\x7e]|\xa1-\xfe])/";
    preg_match_all($re[$charset], $str, $match);
    $slice = join("", array_slice($match[0], $start, $length));
    if ($suffix) return $slice . "…";
    return $slice;
}
```

#### 删除字符串右侧指定字符

```php
/**
 * 删除字符串右侧指定字符
 * @param $string
 * @param $trim
 * @param $encoding
 * @return string
 */
function mb_rtrim($string, $trim, $encoding)
{

    $mask = [];
    $trimLength = mb_strlen($trim, $encoding);
    for ($i = 0; $i < $trimLength; $i++) {
        $item = mb_substr($trim, $i, 1, $encoding);
        $mask[] = $item;
    }

    $len = mb_strlen($string, $encoding);
    if ($len > 0) {
        $i = $len - 1;
        do {
            $item = mb_substr($string, $i, 1, $encoding);
            if (in_array($item, $mask)) {
                $len--;
            } else {
                break;
            }
        } while ($i-- != 0);
    }

    return mb_substr($string, 0, $len, $encoding);
}


$tag = "互联网产品、";
//print_r(mb_rtrim($tag, "、",'utf-8'));
echo rtrim($tag, '、');  // 互联网产�
```



#### 生成随机字符串

```php
/**
 * 产生随机字串，可用来自动生成密码
 * @param string $len 长度
 * @param int $type 字符串类型(0-大小写 1-纯数字 2-纯大写 3-纯小写 4-中文 )
 * @param string $addChars
 * @return false|string
 */
function rand_string($len = 6, $type = 0, $addChars = '')
{
    $str = '';
    switch ($type) {
        case 0:
            $chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' . $addChars;
            break;
        case 1:
            $chars = str_repeat('0123456789', 3);
            break;
        case 2:
            $chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' . $addChars;
            break;
        case 3:
            $chars = 'abcdefghijklmnopqrstuvwxyz' . $addChars;
            break;
        case 4:
            $chars = "们以我到他会作时要动国产的一是工就年阶义发成部民可出能方进在了不和有大这主中人上为来分生对于学下级地个用同行面说种过命度革而多子后自社加小机也经力线本电高量长党得实家定深法表着水理化争现所二起政三好十战无农使性前等反体合斗路图把结第里正新开论之物从当两些还天资事队批点育重其思与间内去因件日利相由压员气业代全组数果期导平各基或月毛然如应形想制心样干都向变关问比展那它最及外没看治提五解系林者米群头意只明四道马认次文通但条较克又公孔领军流入接席位情运器并飞原油放立题质指建区验活众很教决特此常石强极土少已根共直团统式转别造切九你取西持总料连任志观调七么山程百报更见必真保热委手改管处己将修支识病象几先老光专什六型具示复安带每东增则完风回南广劳轮科北打积车计给节做务被整联步类集号列温装即毫知轴研单色坚据速防史拉世设达尔场织历花受求传口断况采精金界品判参层止边清至万确究书术状厂须离再目海交权且儿青才证低越际八试规斯近注办布门铁需走议县兵固除般引齿千胜细影济白格效置推空配刀叶率述今选养德话查差半敌始片施响收华觉备名红续均药标记难存测士身紧液派准斤角降维板许破述技消底床田势端感往神便贺村构照容非搞亚磨族火段算适讲按值美态黄易彪服早班麦削信排台声该击素张密害侯草何树肥继右属市严径螺检左页抗苏显苦英快称坏移约巴材省黑武培著河帝仅针怎植京助升王眼她抓含苗副杂普谈围食射源例致酸旧却充足短划剂宣环落首尺波承粉践府鱼随考刻靠够满夫失包住促枝局菌杆周护岩师举曲春元超负砂封换太模贫减阳扬江析亩木言球朝医校古呢稻宋听唯输滑站另卫字鼓刚写刘微略范供阿块某功套友限项余倒卷创律雨让骨远帮初皮播优占死毒圈伟季训控激找叫云互跟裂粮粒母练塞钢顶策双留误础吸阻故寸盾晚丝女散焊功株亲院冷彻弹错散商视艺灭版烈零室轻血倍缺厘泵察绝富城冲喷壤简否柱李望盘磁雄似困巩益洲脱投送奴侧润盖挥距触星松送获兴独官混纪依未突架宽冬章湿偏纹吃执阀矿寨责熟稳夺硬价努翻奇甲预职评读背协损棉侵灰虽矛厚罗泥辟告卵箱掌氧恩爱停曾溶营终纲孟钱待尽俄缩沙退陈讨奋械载胞幼哪剥迫旋征槽倒握担仍呀鲜吧卡粗介钻逐弱脚怕盐末阴丰雾冠丙街莱贝辐肠付吉渗瑞惊顿挤秒悬姆烂森糖圣凹陶词迟蚕亿矩康遵牧遭幅园腔订香肉弟屋敏恢忘编印蜂急拿扩伤飞露核缘游振操央伍域甚迅辉异序免纸夜乡久隶缸夹念兰映沟乙吗儒杀汽磷艰晶插埃燃欢铁补咱芽永瓦倾阵碳演威附牙芽永瓦斜灌欧献顺猪洋腐请透司危括脉宜笑若尾束壮暴企菜穗楚汉愈绿拖牛份染既秋遍锻玉夏疗尖殖井费州访吹荣铜沿替滚客召旱悟刺脑措贯藏敢令隙炉壳硫煤迎铸粘探临薄旬善福纵择礼愿伏残雷延烟句纯渐耕跑泽慢栽鲁赤繁境潮横掉锥希池败船假亮谓托伙哲怀割摆贡呈劲财仪沉炼麻罪祖息车穿货销齐鼠抽画饲龙库守筑房歌寒喜哥洗蚀废纳腹乎录镜妇恶脂庄擦险赞钟摇典柄辩竹谷卖乱虚桥奥伯赶垂途额壁网截野遗静谋弄挂课镇妄盛耐援扎虑键归符庆聚绕摩忙舞遇索顾胶羊湖钉仁音迹碎伸灯避泛亡答勇频皇柳哈揭甘诺概宪浓岛袭谁洪谢炮浇斑讯懂灵蛋闭孩释乳巨徒私银伊景坦累匀霉杜乐勒隔弯绩招绍胡呼痛峰零柴簧午跳居尚丁秦稍追梁折耗碱殊岗挖氏刃剧堆赫荷胸衡勤膜篇登驻案刊秧缓凸役剪川雪链渔啦脸户洛孢勃盟买杨宗焦赛旗滤硅炭股坐蒸凝竟陷枪黎救冒暗洞犯筒您宋弧爆谬涂味津臂障褐陆啊健尊豆拔莫抵桑坡缝警挑污冰柬嘴啥饭塑寄赵喊垫丹渡耳刨虎笔稀昆浪萨茶滴浅拥穴覆伦娘吨浸袖珠雌妈紫戏塔锤震岁貌洁剖牢锋疑霸闪埔猛诉刷狠忽灾闹乔唐漏闻沈熔氯荒茎男凡抢像浆旁玻亦忠唱蒙予纷捕锁尤乘乌智淡允叛畜俘摸锈扫毕璃宝芯爷鉴秘净蒋钙肩腾枯抛轨堂拌爸循诱祝励肯酒绳穷塘燥泡袋朗喂铝软渠颗惯贸粪综墙趋彼届墨碍启逆卸航衣孙龄岭骗休借" . $addChars;
            break;
        default :
            // 默认去掉了容易混淆的字符oOLl和数字01，要添加请使用addChars参数
            $chars = 'ABCDEFGHIJKMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789' . $addChars;
            break;
    }
    if ($len > 10) { // 位数过长重复字符串一定次数
        $chars = $type == 1? str_repeat($chars, $len) : str_repeat($chars, 5);
    }
    if ($type != 4) {
        $chars = str_shuffle($chars);
        $str = substr($chars, 0, $len);
    } else {
        // 中文随机字
        for($i = 0;$i < $len;$i++) {
            $str .= msubstr($chars, floor(mt_rand(0, mb_strlen($chars, 'utf-8')-1)), 1);
        }
    }
    return $str;
}
```







#### 生成UUID

```php
function uuid()
{
    $charid = md5(uniqid(mt_rand(), true));
    $hyphen = chr(45); // "-"
    $uuid = chr(123)// "{"
    . substr($charid, 0, 8) . $hyphen
    . substr($charid, 8, 4) . $hyphen
    . substr($charid, 12, 4) . $hyphen
    . substr($charid, 16, 4) . $hyphen
    . substr($charid, 20, 12)
    . chr(125); // "}"
    return $uuid;
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



## Http请求



```php
/**
 * 网络请求
 * @param $url
 * @param $params
 * @param $options
 * @return bool|string|null
 */
function curl($url,$params = [],$options = []){
    $curlInstance = curl_init($url);
    $defaultOpt = array(
        CURLOPT_POST=>1,
        CURLOPT_RETURNTRANSFER=>1,
        CURLOPT_TIMEOUT=>3,
    );
    if(is_array($options) && !empty($options) ){
        foreach($options as $k=>$v){
            $defaultOpt[$k]=$v;
        }
    }
    foreach($defaultOpt as $k=>$v){
        curl_setopt($curlInstance,$k,$v);
    }
    if($defaultOpt[CURLOPT_POST] && !empty($params)){ //如果输入的是Post请求，并设置了请求参数，将post内容封装到CURLOPT_POSTFIELDS中
        if(is_array($params)){
            $content=http_build_query($params);
        }else{
            $content=$params;
        }
        curl_setopt($curlInstance,CURLOPT_POSTFIELDS, $content);
    }

    $count=0;
    $ret = null;
    while($count<3){
        $ret = curl_exec($curlInstance);
        $errno = curl_errno($curlInstance);
        $errmsg = curl_error($curlInstance);
        if(!$errno) {
            break;
        }
        //此处要记录错误日志
        $count++;
    }
    curl_close($curlInstance);
    return $ret;
}
```





## 时间

#### 获取某年某月的天数

```php
/**
 * 获取某年某月的天数
 * @param string $year 年份 
 * @param string $month 月份
 * @return int 天数
 */
function dayNum($year,$month)
{
    $big_month=[1,3,5,7,8,10,12];
    $sm_month=[4,6,9,11];
    if(in_array($month,$big_month))
    {
        $day_num=31;
    }
    else if(in_array($month,$sm_month))
    {
        $day_num=30;
    }
    else 
    {
        if($year%4==0 && ($year%100!=0 || $year%400==0))//闰年
        {
            $day_num=29;
        }
        else
        {
            $day_num=28;
        }
    }
    return $day_num;
}
```

#### 判断当前年是否是闰年

```php
/**
 * 判断当前年是否是闰年
 * @param $year
 * @return bool
 */
function isLeapYear($year)
{
    $ts = mktime(0, 0, 0, 2, 1, $year);
    return date('L', $ts) == 1;
//    return date('t', $ts) == 29;
}
```

























