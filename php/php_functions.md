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

#### 手机号脱敏

```php
function maskMobile($mobile) {
    $pattern = "/(1\d{1,2})\d\d(\d{0,3})/";
    $replacement = "\$1****\$3";
    $mobile = preg_replace($pattern, $replacement, $mobile);
    return $mobile;
}
```





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

function cutstr( $string, $length, $dot = '...', $charset = 'utf-8' ) {
        if ( strlen( $string ) <= $length )
            return $string;

        $pre = chr( 1 );
        $end = chr( 1 );
        $string = str_replace( array ( '&amp;' , '&quot;' , '&lt;' , '&gt;' ), array ( $pre . '&' . $end , $pre . '"' . $end , $pre . '<' . $end , $pre . '>' . $end ), $string );

        $strcut = '';
        if ( strtolower( $charset ) == 'utf-8' ) {

            $n = $tn = $noc = 0;
            while ( $n < strlen( $string ) ) {

                $t = ord( $string[$n] );
                if ( $t == 9 || $t == 10 || ( 32 <= $t && $t <= 126 ) ) {
                    $tn = 1;
                    $n ++;
                    $noc ++;
                } elseif ( 194 <= $t && $t <= 223 ) {
                    $tn = 2;
                    $n += 2;
                    $noc += 2;
                } elseif ( 224 <= $t && $t <= 239 ) {
                    $tn = 3;
                    $n += 3;
                    $noc += 2;
                } elseif ( 240 <= $t && $t <= 247 ) {
                    $tn = 4;
                    $n += 4;
                    $noc += 2;
                } elseif ( 248 <= $t && $t <= 251 ) {
                    $tn = 5;
                    $n += 5;
                    $noc += 2;
                } elseif ( $t == 252 || $t == 253 ) {
                    $tn = 6;
                    $n += 6;
                    $noc += 2;
                } else {
                    $n ++;
                }

                if ( $noc >= $length ) {
                    break;
                }

            }
            if ( $noc > $length ) {
                $n -= $tn;
            }

            $strcut = substr( $string, 0, $n );

        } else {
            for ( $i = 0; $i < $length; $i ++ ) {
                $strcut .= ord( $string[$i] ) > 127 ? $string[$i] . $string[++ $i] : $string[$i];
            }
        }

        $strcut = str_replace( array ( $pre . '&' . $end , $pre . '"' . $end , $pre . '<' . $end , $pre . '>' . $end ), array ( '&amp;' , '&quot;' , '&lt;' , '&gt;' ), $strcut );

        $pos = strrpos( $strcut, chr( 1 ) );
        if ( $pos !== false ) {
            $strcut = substr( $strcut, 0, $pos );
        }
        return $strcut . $dot;
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



// 生成随机数, 可用于生成验证码
function getRand($len) {
    $d='';
    for($i=0; $i < $len; ++$i) {
        if( rand(0,9) < 6 ) {
            // Digits   数字 1-9  除去0
            $d .= chr( ord('1') + rand(0,8) );
        } else {
            // Letters  //获取 除o字母(小写字母)
            do {
                $offset = rand(0,25);
            } while ( $offset==14 );
            $d .= chr( ord('a') + $offset );
        }
    }
    return $d;
}

// 生成指定长度的纯数字随机字符串
function generateRandNumString($len)
{
    $min = ord('0');
    $max = ord('9');
    $value = '';
    for ($i = 0; $i < $len; $i++)
    {
        $value .= chr(rand($min, $max));
    }
    return $value;
}


function get_code($len){
	$CHAR_ARR = array('1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','X','Y','Z','W','S','R','T');
	$CHAR_ARR_LEN = count($CHAR_ARR) - 1;
	$code = '';
	while(--$len >= 0){ 
		$code .= $CHAR_ARR[rand(0,$CHAR_ARR_LEN)]; 
	}
	return $code;
}


```

#### 生成订单号

```php
function createOrderNo($datetime=null)
    {
        $datetime = $datetime ? date('ymdHis',strtotime($datetime)) : date('YmdHis');
        return $datetime.substr(crc32(uniqid(true)), -4);
    }
```





#### 是否包含中文

```php
/**
 * 是否包含中文
 * @param string $str  字符串
 * @param boolean $isAll 是否全部包含
 * @return false|int
 */
function hasChinese($str, $isAll=false): bool
{
    $ret = preg_match("/[\x7f-\xff]/", $str);
    if($isAll){
        $ret = preg_match("/^[\x7f-\xff]+$/", $str);  // 全部为中文
    }
    return boolval($ret);
}
```

#### 判断是否是字母

```php
function isLetter($str)
{
    $ascii = ord($str);
    return (($ascii >= 65 && $ascii <=90) || ($ascii >=97 && $ascii<=122));
}
// 或直接使用函数ctype_alpha
```

#### 获取字符串拼音首字母

```php
function Pinyin($_String, $first = 0, $_Code='gb2312'){
    $_DataKey = 	"a|ai|an|ang|ao|ba|bai|ban|bang|bao|bei|ben|beng|bi|bian|biao|bie|bin|bing|bo|bu|ca|cai|can|cang|cao|ce|ceng|cha".
        "|chai|chan|chang|chao|che|chen|cheng|chi|chong|chou|chu|chuai|chuan|chuang|chui|chun|chuo|ci|cong|cou|cu|".
        "cuan|cui|cun|cuo|da|dai|dan|dang|dao|de|deng|di|dian|diao|die|ding|diu|dong|dou|du|duan|dui|dun|duo|e|en|er".
        "|fa|fan|fang|fei|fen|feng|fo|fou|fu|ga|gai|gan|gang|gao|ge|gei|gen|geng|gong|gou|gu|gua|guai|guan|guang|gui".
        "|gun|guo|ha|hai|han|hang|hao|he|hei|hen|heng|hong|hou|hu|hua|huai|huan|huang|hui|hun|huo|ji|jia|jian|jiang".
        "|jiao|jie|jin|jing|jiong|jiu|ju|juan|jue|jun|ka|kai|kan|kang|kao|ke|ken|keng|kong|kou|ku|kua|kuai|kuan|kuang".
        "|kui|kun|kuo|la|lai|lan|lang|lao|le|lei|leng|li|lia|lian|liang|liao|lie|lin|ling|liu|long|lou|lu|lv|luan|lue".
        "|lun|luo|ma|mai|man|mang|mao|me|mei|men|meng|mi|mian|miao|mie|min|ming|miu|mo|mou|mu|na|nai|nan|nang|nao|ne".
        "|nei|nen|neng|ni|nian|niang|niao|nie|nin|ning|niu|nong|nu|nv|nuan|nue|nuo|o|ou|pa|pai|pan|pang|pao|pei|pen".
        "|peng|pi|pian|piao|pie|pin|ping|po|pu|qi|qia|qian|qiang|qiao|qie|qin|qing|qiong|qiu|qu|quan|que|qun|ran|rang".
        "|rao|re|ren|reng|ri|rong|rou|ru|ruan|rui|run|ruo|sa|sai|san|sang|sao|se|sen|seng|sha|shai|shan|shang|shao|".
        "she|shen|sheng|shi|shou|shu|shua|shuai|shuan|shuang|shui|shun|shuo|si|song|sou|su|suan|sui|sun|suo|ta|tai|".
        "tan|tang|tao|te|teng|ti|tian|tiao|tie|ting|tong|tou|tu|tuan|tui|tun|tuo|wa|wai|wan|wang|wei|wen|weng|wo|wu".
        "|xi|xia|xian|xiang|xiao|xie|xin|xing|xiong|xiu|xu|xuan|xue|xun|ya|yan|yang|yao|ye|yi|yin|ying|yo|yong|you".
        "|yu|yuan|yue|yun|za|zai|zan|zang|zao|ze|zei|zen|zeng|zha|zhai|zhan|zhang|zhao|zhe|zhen|zheng|zhi|zhong|".
        "zhou|zhu|zhua|zhuai|zhuan|zhuang|zhui|zhun|zhuo|zi|zong|zou|zu|zuan|zui|zun|zuo";

    $_DataValue = "-20319|-20317|-20304|-20295|-20292|-20283|-20265|-20257|-20242|-20230|-20051|-20036|-20032|-20026|-20002|-19990".
        "|-19986|-19982|-19976|-19805|-19784|-19775|-19774|-19763|-19756|-19751|-19746|-19741|-19739|-19728|-19725".
        "|-19715|-19540|-19531|-19525|-19515|-19500|-19484|-19479|-19467|-19289|-19288|-19281|-19275|-19270|-19263".
        "|-19261|-19249|-19243|-19242|-19238|-19235|-19227|-19224|-19218|-19212|-19038|-19023|-19018|-19006|-19003".
        "|-18996|-18977|-18961|-18952|-18783|-18774|-18773|-18763|-18756|-18741|-18735|-18731|-18722|-18710|-18697".
        "|-18696|-18526|-18518|-18501|-18490|-18478|-18463|-18448|-18447|-18446|-18239|-18237|-18231|-18220|-18211".
        "|-18201|-18184|-18183|-18181|-18012|-17997|-17988|-17970|-17964|-17961|-17950|-17947|-17931|-17928|-17922".
        "|-17759|-17752|-17733|-17730|-17721|-17703|-17701|-17697|-17692|-17683|-17676|-17496|-17487|-17482|-17468".
        "|-17454|-17433|-17427|-17417|-17202|-17185|-16983|-16970|-16942|-16915|-16733|-16708|-16706|-16689|-16664".
        "|-16657|-16647|-16474|-16470|-16465|-16459|-16452|-16448|-16433|-16429|-16427|-16423|-16419|-16412|-16407".
        "|-16403|-16401|-16393|-16220|-16216|-16212|-16205|-16202|-16187|-16180|-16171|-16169|-16158|-16155|-15959".
        "|-15958|-15944|-15933|-15920|-15915|-15903|-15889|-15878|-15707|-15701|-15681|-15667|-15661|-15659|-15652".
        "|-15640|-15631|-15625|-15454|-15448|-15436|-15435|-15419|-15416|-15408|-15394|-15385|-15377|-15375|-15369".
        "|-15363|-15362|-15183|-15180|-15165|-15158|-15153|-15150|-15149|-15144|-15143|-15141|-15140|-15139|-15128".
        "|-15121|-15119|-15117|-15110|-15109|-14941|-14937|-14933|-14930|-14929|-14928|-14926|-14922|-14921|-14914".
        "|-14908|-14902|-14894|-14889|-14882|-14873|-14871|-14857|-14678|-14674|-14670|-14668|-14663|-14654|-14645".
        "|-14630|-14594|-14429|-14407|-14399|-14384|-14379|-14368|-14355|-14353|-14345|-14170|-14159|-14151|-14149".
        "|-14145|-14140|-14137|-14135|-14125|-14123|-14122|-14112|-14109|-14099|-14097|-14094|-14092|-14090|-14087".
        "|-14083|-13917|-13914|-13910|-13907|-13906|-13905|-13896|-13894|-13878|-13870|-13859|-13847|-13831|-13658".
        "|-13611|-13601|-13406|-13404|-13400|-13398|-13395|-13391|-13387|-13383|-13367|-13359|-13356|-13343|-13340".
        "|-13329|-13326|-13318|-13147|-13138|-13120|-13107|-13096|-13095|-13091|-13076|-13068|-13063|-13060|-12888".
        "|-12875|-12871|-12860|-12858|-12852|-12849|-12838|-12831|-12829|-12812|-12802|-12607|-12597|-12594|-12585".
        "|-12556|-12359|-12346|-12320|-12300|-12120|-12099|-12089|-12074|-12067|-12058|-12039|-11867|-11861|-11847".
        "|-11831|-11798|-11781|-11604|-11589|-11536|-11358|-11340|-11339|-11324|-11303|-11097|-11077|-11067|-11055".
        "|-11052|-11045|-11041|-11038|-11024|-11020|-11019|-11018|-11014|-10838|-10832|-10815|-10800|-10790|-10780".
        "|-10764|-10587|-10544|-10533|-10519|-10331|-10329|-10328|-10322|-10315|-10309|-10307|-10296|-10281|-10274".
        "|-10270|-10262|-10260|-10256|-10254";

    $_TDataKey   = explode('|', $_DataKey);
    $_TDataValue = explode('|', $_DataValue);
    $_Data = array_combine($_TDataKey, $_TDataValue);

    arsort($_Data);
    reset($_Data);

    if($_Code != 'gb2312'){
        $_String = _U2_Utf8_Gb($_String);
    }

    $_Res = '';
    for($i=0; $i<strlen($_String); $i++){
        $_P = ord(substr($_String, $i, 1));
        if($_P>160) {
            $_Q = ord(substr($_String, ++$i, 1)); $_P = $_P*256 + $_Q - 65536;
        }

        $_Res .= _Pinyin($_P, $_Data, $first);
    }
    var_dump($_Res);
    return preg_replace("/[^a-z0-9]*/", '', $_Res);
}


function _Pinyin($_Num, $_Data, $first){
    if ($_Num>0 && $_Num<160 ){
        return chr($_Num);
    }elseif($_Num<-20319 || $_Num>-10247){
        return '';
    }else{
        foreach($_Data as $k=>$v){
            if($v<=$_Num) break;
        }

        // 只返回第一个字母的小写形式
        if($first){
            return strtolower(substr($k, 0, 1));
        }

        return $k;
    }
}


function _U2_Utf8_Gb($_C){
    $_String = '';
    if($_C < 0x80){
        $_String .= $_C;
    }elseif($_C < 0x800){
        $_String .= chr(0xC0 | $_C>>6);
        $_String .= chr(0x80 | $_C & 0x3F);
    }elseif($_C < 0x10000){
        $_String .= chr(0xE0 | $_C>>12);
        $_String .= chr(0x80 | $_C>>6 & 0x3F);
        $_String .= chr(0x80 | $_C & 0x3F);
    }elseif($_C < 0x200000){
        $_String .= chr(0xF0 | $_C>>18);
        $_String .= chr(0x80 | $_C>>12 & 0x3F);
        $_String .= chr(0x80 | $_C>>6 & 0x3F);
        $_String .= chr(0x80 | $_C & 0x3F);
    }

    return iconv('UTF-8', 'GB2312', $_String);
}

echo Pinyin('蓝狼的爱', 1, 'utf-8');  // hnbgy
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


function guid(){
    if (function_exists('com_create_guid')){
        return com_create_guid();
    }else{
        mt_srand((double)microtime()*10000);//optional for php 4.2.0 and up.
        $charid = strtoupper(md5(uniqid(rand(), true)));
        $hyphen = chr(45);// "-"
        $uuid = chr(123)// "{"
                .substr($charid, 0, 8).$hyphen
                .substr($charid, 8, 4).$hyphen
                .substr($charid,12, 4).$hyphen
                .substr($charid,16, 4).$hyphen
                .substr($charid,20,12)
                .chr(125);// "}"
        return $uuid;
    }
}

```

#### 生成文件名ID

```php
/**
* unique_ID
* 生成16位以上唯一ID
* @param int $length 不含前缀的长度，最小14，建议16+
* @param str $prefix 前缀
* @return str $id
*/
function unique_ID($length = 16,$prefix = ''){
    $id = $prefix;
    $addLength = $length - 13;
    $id .= uniqid();
    if (function_exists('random_bytes')) {
        $id .= substr(bin2hex(random_bytes(ceil(($addLength) / 2))),0,$addLength);
    } elseif (function_exists('openssl_random_pseudo_bytes')) {
        $id .= substr(bin2hex(openssl_random_pseudo_bytes(ceil($addLength / 2))),0,$addLength);
    } else {
        $id .= mt_rand(1*pow(10,($addLength)),9*pow(10,($addLength)));
    }
    return $id;
}
```





#### 驼峰转下划线

```php
function camel2Flat($word) {
    return strtolower(preg_replace('/(\w)([A-Z])(\w)/', '\1_\2\3', $word));
}
```

#### 下划线转驼峰

```php
function Flat2Camel($word) {
    $arr = explode('_', $word);
    $string = "";
    foreach ($arr as $value) {
        $string .=ucfirst($value);
    }
    return lcfirst($string);
}
```

#### 首字母转小写

```php
function lcfirst($word) {
    $word[0] = strtolower($word[0]);
    return (string) $word;
}
```

#### 字符集转换

```php
function autoCharset ($string, $from = 'gbk', $to = 'utf-8')
    {
        $from = strtoupper($from) == 'UTF8' ? 'utf-8' : $from;
        $to = strtoupper($to) == 'UTF8' ? 'utf-8' : $to;
        if (strtoupper($from) === strtoupper($to) || empty($string) || (is_scalar($string) && ! is_string($string))) {
            //如果编码相同或者非字符串标量则不转换
            return $string;
        }
        if (is_string($string)) {
            if (function_exists('mb_convert_encoding')) {
                return mb_convert_encoding($string, $to, $from);
            } elseif (function_exists('iconv')) {
                return iconv($from, $to, $string);
            } else {
                return $string;
            }
        } elseif (is_array($string)) {
            foreach ($string as $key => $val) {
                $_key = self::autoCharset($key, $from, $to);
                $string[$_key] = self::autoCharset($val, $from, $to);
                if ($key != $_key)
                    unset($string[$key]);
            }
            return $string;
        } else {
            return $string;
        }
    }
```

#### 清理特殊字符

```php
function clean_chars($str)
{
  $chars_map = array("'", "&", ";", "--", "<", ">", "(", ")", "=", "\"", ",", "[", "]", "{", "}", '\\');
  return str_replace($chars_map, '', $str);
}
```

#### 过滤emoji

```php
function filterEmoji($text)
{
    // Match Emoticons
    $regexEmoticons = '/[\x{1F600}-\x{1F64F}]/u';
    $text = preg_replace($regexEmoticons, '', $text);

    // Match Miscellaneous Symbols and Pictographs
    $regexSymbols = '/[\x{1F300}-\x{1F5FF}]/u';
    $text = preg_replace($regexSymbols, '', $text);

    // Match Transport And Map Symbols
    $regexTransport = '/[\x{1F680}-\x{1F6FF}]/u';
    $text = preg_replace($regexTransport, '', $text);

    // Match Miscellaneous Symbols
    $regexMisc = '/[\x{2600}-\x{26FF}]/u';
    $text = preg_replace($regexMisc, '', $text);

    // Match Dingbats
    $regexDingbats = '/[\x{2700}-\x{27BF}]/u';
    $text = preg_replace($regexDingbats, '', $text);

    $text = preg_replace_callback(
        '/./u',
        function (array $match) {
            return strlen($match[0]) >= 4 ? '' : $match[0];
        },
        $text);

    //去除空格
    if(!empty($text)){
        $text = str_replace(' ', '',$text);
    }

    return $text;
}


function filterEmoji($str)  
    {  
        $str = preg_replace_callback(  
        '/./u',  
        function (array $match) {  
            return strlen($match[0]) >= 4 ? '' : $match[0];  
        },  
        $str);  
      
      return $str;  
    }
```





#### 是否以某个字符串开头的字符串

```php
function startsWith($haystack, $needle) {
    $length = strlen($needle);
    return (substr($haystack, 0, $length) === $needle);
}
```



#### 是否以某个字符串结尾的字符串

```php
function str_endWith($str,$subStr){
	return substr($str, -(strlen($subStr)))==$subStr;
}
```



#### 过滤乱码

```php
/**
 * 过滤乱码
 * @param $str 
 * @param $debug
 */
function filterMessChars($str, $debug=0)
{
	$str = preg_replace('/&lt;a href=&quot;.*?&quot; target=&quot;_blank&quot;&gt;.*?&lt;\/a&gt;/si', '', $str);
	//if($debug)echo $str."<br>\n";  
	$new_str = "";
	for($i = 0; $i < strlen($str); $i++)
	{	
        	$value = ord($str[$i]);
        	if($value > 127){
            		if($value >= 192 && $value <= 223) $c = 2;
            		elseif($value >= 224 && $value <= 239) $c = 3;
            		elseif($value >= 240 && $value <= 247) $c = 4;
            		else continue;
        	}
		else
			$c = 1;
		if(($c == 3 || $c == 1) && $value != 237)
			$new_str .= substr($str, $i, $c);
	//	if($debug)
	//		echo substr($str, $i, $c) . ":$c:" . $value."<br>\n";
	    	$i += $c - 1;
	}
	return $new_str;
}
```

#### 放置SQL注入处理

```php
function clean($input)
{
    if (is_array($input))
    {
        foreach ($input as $key => $val)
         {
             $output[$key] = clean($val);
         }
    }
    else
    {
        $output = (string) $input;
        // if magic quotes is on then use strip slashes
        if (get_magic_quotes_gpc())
        {
            $output = stripslashes($output);
        }
        $output = htmlentities($output, ENT_QUOTES, 'UTF-8');
    }
// return the clean text
    return $output;
}
```



#### 提取文本中的图片标签

```php
function imgs($string){
    //preg_match_all函数进行全局正则表达式匹配。
//     $param1 = "/<img([^>]*)\s*src=('|\")([^'\"]+)('|\")/";  //带引号
//     $param2 = "/<img([^>]*)\ssrc=([^\s>]+)/";               //不带引号
//    $param3 = '/<img.*?src=[\'|\"](.*?(?:[\.gif|\.jpg]))[\'|\"].*?[\/]? >/i';
    $param3 = '/<img.*?src=[\'|\"](.*?)[\'|\"].*?[\/]?>/i';
    //这个获取图片的全部标签
    preg_match_all($param3,$string,$matches);//不带引号
    return $matches[0];//图片标签 //$matches[1] 链接地址
}
```



#### 提取字符串中的URL

```php
function getUrls($string)
{
    $regex = '/https?\:\/\/[^\" ]+/i';
    preg_match_all($regex, $string, $matches);
    return ($matches[0]);
}
```



#### 邮箱编码处理

```php
// 把邮箱地址转换成HTML ASCII编码的主要作用是防止网页邮箱采集器，比如常见的把@替换为#、[@]或干脆直接用图片都是为了防止网页邮箱采集器
echo encodeEmail('kevin@example.org');

/**
 *
 * Return ASCII value for web use
 *
 * @param string
 *
 * @return string
 *
 */
function makeASCII($char=0){
  return '&#'.ord($char).';';
}

/**
 *
 * @Encode an email to ascii
 *
 * @parma string 
 *
 * @return string
 *
 */
function encodeEmail($email){

if(filter_var($email, FILTER_VALIDATE_EMAIL) !== FALSE)
    {
    $charArray = str_split($email);
    $encodedArray = filter_var($charArray, FILTER_CALLBACK, array('options'=>"makeASCII"));
    $encodedString = implode('',$encodedArray);
    return '<a href="mailto:'.$encodedString.'">'.$encodedString.'</a>';
    }
else
  {
  return false;
  } 
}
```





## 数组

#### 从二维数组中提取key

```php
/**
 * 从二维数组中取出自己要的KEY值(去除为空字符并根据结果排序)
 * @param  array $arrData
 * @param string $key
 * @param $im true 返回逗号分隔
 * @return array
 */
function filter_value($arrData, $key, $im = false)
{
    $re = [];
    foreach ($arrData as $k => $v) {
        if (isset($v[$key])) $re[] = $v[$key];
    }
    if (!empty($re)) {
        $re = array_flip(array_flip($re));
        sort($re);
    }

    return $im ? implode(',', $re) : $re;
}
```

#### 通过数组中的值获取对应的key

```php
// 通过数组的值获取数组的 key
function getArrayKey($arr, $value) {
    if(!is_array($arr)){
        return null;
    }

    foreach($arr as $k =>$v) {
        $return = getArrayKey($v, $value);
        if($v == $value){
            return $k;
        }

        if(!is_null($return)){
            return $return;
        }
    }
}
```

#### 多维数组合并

```php
/**
 * 多维数组合并（支持多数组）
 * @return array
 */
function array_merge_multi()
{
    $args = func_get_args();
    $array = [];
    foreach ($args as $arg) {
        if (is_array($arg)) {
            foreach ($arg as $k => $v) {
                if (is_array($v)) {
                    $array[$k] = isset($array[$k]) ? $array[$k] : [];
                    $array[$k] = array_merge_multi($array[$k], $v);
                } else {
                    $array[$k] = $v;
                }
            }
        }
    }

    return $array;
}
```

#### 多维数组转一维数组(索引数组)

```php
function reduceArray($array) {
	    $return = [];
	    array_walk_recursive($array, function ($x) use (&$return) {
	        $return[] = $x;
	    });
	    return $return;
}
》》》
$data = [
    ['php','python','golang'],
    ['mysql','sqlite','mongodb','redis','Memcache']
];
print_r(reduceArray($data));
>>> Array
(
    [0] => php
    [1] => python
    [2] => golang
    [3] => mysql
    [4] => sqlite
    [5] => mongodb
    [6] => redis
    [7] => Memcache
)
```





#### 数组与对象间的转换

```php
// Convert object to array
function object2Array($obj) {
    if(is_object($obj)){
        $obj = get_object_vars($obj);
    }
    return is_array($obj) ? array_map(__FUNCTION__, $obj):$obj;
}
// Convert array to object
function array2Object($arr) {
    return is_array($arr) ? (object) array_map(__FUNCTION__, $arr):$arr;
}
```

#### 判断是否是多维数组

```php
function isMultiArray($arr){
    if(empty($arr)) return false;

    if(is_array($arr)){
        foreach($arr as $a){
            if(is_array($a)){
                return true;
            }
        }
        return false;
    }
    return false;
}
```

#### 多维数组去重

```php
function multiArrayUnique($arr){
    foreach($arr as $k => $v){
        foreach($arr as $key => $value){
            if($k != $key){
                $v1 = json_encode($v);
                $v2 = json_encode($value);
                if($v1 == $v2){
                    unset($arr[$k]);
                }
            }
        }
    }
    sort($arr);
    return $arr;
}
```

#### 生成指定范围的不重复的随机数

```php
/**
 * 生成一定数量的不重复随机数
 * @param  integer $min 最小值
 * @param  integer $max 最大值
 * @param  integer $num 随机数数量
 * @return array        返回值
 */
function generateUniqueRand(int $min, int $max,int $num)
{
    $count = 0;
    $return = [];
    if(($max-$min+1)<$num){
        return $return;
    }

    while ($count < $num) {
        $return[] = mt_rand($min, $max);
        $return   = array_flip(array_flip($return));
        $count    = count($return);
    }
    shuffle($return);
    return $return;
}
```

#### 数组排序

```php
//二维数组排序， $arr是数据，$keys是排序的健值，$order是排序规则，0是升序，1是降序
function array_sort($arr, $keys, $order=0) {
        if (!is_array($arr)) {
                return false;
        }
        if(count($arr)==0)
        {
        	return array();
        }
        $keysvalue = array();
        foreach($arr as $key => $val) {
                $keysvalue[$key] = $val[$keys];
        }
        if($order == 0){
                asort($keysvalue);
        }else {
                arsort($keysvalue);
        }
        reset($keysvalue);
        $keysort=array();
        foreach($keysvalue as $key => $vals) {
                $keysort[$key] = $key;
        }
        
        $new_array=array();
        foreach($keysort as $key => $val) {
                $new_array[$key] = $arr[$val];
        }
        return $new_array;
}
```

#### 数组中数据求和

```php
/**
 * 数组中数据的求和（支持多维数组）
 * @param array $array
 * @return int|mixed
 */
function arraySum(array $array)
{
    $total = 0;
    foreach(new RecursiveIteratorIterator( new RecursiveArrayIterator($array) ) as $num){
        $total += $num;
    }
    return $total;
}

》》》
$arr = [[11,22],33, [44,55,[66,77]]];
print_r(arraySum($arr));
>>> 308
```

#### 提取数组中指定字段数据

```php
/**
 * 过滤并获取有用数据
 * @param  array $data      原数据
 * @param  array $standard  保留的参数
 */
function filterData($data, array $standard){
    if(empty($data) || !is_array($data) || !is_array($standard)) return [];

    $standardArr = array_fill_keys($standard, '');

    $data = array_intersect_key($data,$standardArr);

    return array_merge($standardArr,$data);
}

》》》
$arr = ['name'=>'xing','age'=>23,'sex'=>1];
$standard = ['age'];


$ret = filterData($arr, $standard);
var_dump($ret);
>>> array(1) {
  'age' =>
  int(23)
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


function redirect($url)
{
        if (headers_sent()) {
            echo '<html><head><meta http-equiv="refresh" content="0;URL='.$url.'" /></head></html>';
            exit;
        }
        else{
            header("HTTP/1.1 301 Moved Permanently");
            header("Location: {$url}");
            exit; 
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

#### 生成短链接

```php
function code62($x)
{
    $show = '';
    while ($x > 0) {
        $s = $x % 62;
        if ($s > 35) {
            $s = chr($s + 61);
        } elseif ($s > 9 && $s <= 35) {
            $s = chr($s + 55);
        }
        $show .= $s;
        $x = floor($x / 62);
    }
    return $show;
}

function shorturl($url){
    $url=crc32($url);
    $result=sprintf("%u",$url);
    return code62($result);
}

// 使用场景, 例如将长的url的该压缩后的单独存一个字段, 方便进行查询
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

#### 邮箱验证

```php
function isEmail($email)
{
		$chars = "/^([a-z0-9+_]|\\-|\\.)+@(([a-z0-9_]|\\-)+\\.)+[a-z]{2,6}\$/i";
	    if (strpos($email, '@') !== false && strpos($email, '.') !== false)
	    {
	    	if (preg_match($chars, $email))
	    	{
	    		return true;
	    	} 
	    	else
	    	{
	    		return false;
	    	}
	    } 
	    else
	    {
	    	return false;
	    }
}


function isEmail($vStr)
{
	return preg_match('/^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/', $vStr);
}
```

#### 手机号验证

```php
function isMobile($mobile)
{
		if (empty($mobile)) return false;
		
		if(preg_match('/^[1]{1}[3|4|5|8]{1}[0-9]{9}$/', $mobile))
		{
			return true;
		}
		else
		{
			return false;
		}
}
```

#### 网址验证

```php
function url( $str ) {
    if ( empty( $str ) )
        return true;

    return preg_match( '#(http|https|ftp|ftps)://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?#i', $str ) ? true : false;
}
```

#### 判断操作系统

```php
// 是否是Linux
function isLinux() {return strtoupper(PHP_OS) === 'LINUX';}

// 是否是Windows
function isWin() {return strtoupper(substr(PHP_OS, 0, 3)) === 'WIN';}
```









## Http请求

#### 网络请求

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

#### get请求

```php
/**
 * 统一封装的file_get_contents
 * @param  string  $url 请求url
 * @param  integer $timeout 超时时间
 * @param  array   $header 请求头部
 * @return 
 */
function pft_file_get_contents($url, $timeout = 10, $header = []){
    $url     = strval($url);
    $timeout = intval($timeout);
    $timeout = $timeout <= 0 ? 10 : $timeout;

    $contextOptions = [
        'http' => ['timeout' => $timeout]
    ];
    if($header) {
        $contextOptions['http']['header'] = $header;
    }

    $context = stream_context_create($contextOptions);
    $res = file_get_contents($url, false, $context);
    return $res;
}
```





#### post请求

```php
/**
 * curl请求
 * @param  string  $url     地址
 * @param  array   $data    post数据
 * @param  array   $options 参数数据
 * @param  boolean $isTry   是否错误重试
 */
function cUrl($url,$data = null,$options = [],$isTry = false)
{
    $ch = curl_init();

    // 默认配置
    $opts = [
        CURLOPT_URL             =>  $url,
        CURLOPT_HEADER          =>  0,
        CURLOPT_TIMEOUT         =>  10, //10s
        CURLOPT_RETURNTRANSFER  =>  true, //不直接输出
    ];

    $ssl = stripos($url,'https://') === 0;
    if($ssl){
        $opts[CURLOPT_SSL_VERIFYHOST] = false;
        $opts[CURLOPT_SSL_VERIFYPEER] = false;
    }

    if( is_array($data) ){
        if( !empty($data) ){
            $data = http_build_query($data);
        }

        $opts[CURLOPT_POST]         = true;
        $opts[CURLOPT_POSTFIELDS]   = $data;
    }

    $options += $opts;

    curl_setopt_array($ch,$options);

    $count = 0;
    while ($count < 3) {
        $data = curl_exec($ch);
        if( !curl_errno($ch) ){
            break;
        }

        $data = 'Error:'.curl_errno($ch).curl_error($ch);
        $count ++;
    }

    curl_close($ch);
    return $data;
}

// 简单post请求
function curl( $url, $postStr )
    {
        $curlPost = $postStr;
        $ch = curl_init();//初始化curl
        curl_setopt($ch,CURLOPT_URL,$url);//抓取指定网页
        curl_setopt($ch, CURLOPT_HEADER, 0);//设置header
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);//要求结果为字符串且输出到屏幕上
        curl_setopt($ch, CURLOPT_POST, 1);//post提交方式
        curl_setopt($ch, CURLOPT_POSTFIELDS, $curlPost);
        $data = curl_exec($ch);//运行curl
        curl_close($ch);
        return $data;
    }


/**
 * CURL 提交请求数据
 * @param string $url 请求URL
 * @param string $postData 请求发送的数据
 * @param int $port 请求端口
 * @param int $timeout 超时时间
 * @param array $headers 请求头信息
 * @return bool|mixed
 */
function curl_post($url, $postData, $port = 80, $timeout = 25, $headers = []) {
    //超时时间处理
    $timeout = intval($timeout);
    $timeout = $timeout <= 0 ? 25 : $timeout;

    $ch       = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_PORT, $port);
    curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    if ((is_array($headers) || is_object($headers)) && count($headers)) {
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    }

    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    $res = curl_exec($ch);

    //错误处理
    $errCode = curl_errno($ch);
    if ($errCode > 0) {
        curl_close($ch);
        return false;
    } else {
        //获取HTTP码
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        if ($httpCode != 200) {
            curl_close($ch);
            return false;
        } else {
            curl_close($ch);
            return $res;
        }
    }
}

/**
     * curl操作
     * @param  string  $url    地址 
     * @param  [type]  $post   post参数
     * @param  array   $header Header头
     * @param  integer $timeout 超时时间
     */
    function httpCurl($url, $post=null, $header=[], $timeout=5):array
    {
        $ch = curl_init(); // 启动一个CURL会话
        curl_setopt($ch, CURLOPT_URL, $url);// 要访问的地址
        curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);// 设置超时限制防止死循环
        if ($header)
            curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
        if ($post)
        {
            curl_setopt($ch, CURLOPT_POST, true);// 发送一个常规的Post请求
            curl_setopt($ch, CURLOPT_POSTFIELDS, is_array($post) ? http_build_query($post) : $post);// Post提交的数据包
        }

        curl_setopt($ch, CURLOPT_HEADER, false);// 显示返回的Header区域内容
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);// 获取的信息以文件流的形式返回
        $content = curl_exec($ch); // 执行操作
    
        if($errno = curl_errno($ch) ){
            $errmsg = curl_error($ch);
            return [$errno, $errmsg,curl_getinfo($ch)];
        }
        curl_close($ch);
        
        return [null, $content];
    }




```

#### soap请求

```php
/**
 * 统一封装的SOAP客户端封装，有些系统还在使用soap协议提供接口
 * $soapClient = new PftSoapClient('xxx.wsdl');
 * $soapClient->setTimeout(25);
 * $soapClient->getMyMoney($params);
 */
class PftSoapClient extends \SoapClient {
    //超时的时间
    private $timeout = 0;

    //设置超时时间
    public function setTimeout($timeout) {
        $timeout = intval($timeout);
        $timeout = $timeout <= 0 ? 25 : $timeout;

        $this->timeout = $timeout;
    }

    //请求接口
    public function __doRequest($request, $location, $action, $version, $oneWay = FALSE) {
        if ($this->timeout <= 0) {
            //使用默认的方式
            $res = parent::__doRequest($request, $location, $action, $version, $oneWay);
        } else {
            //使用添加了超时的方式
            $socketTime = ini_get('default_socket_timeout');
            ini_set('default_socket_timeout', $this->timeout);
            $res = parent::__doRequest($request, $location, $action, $version, $oneWay);
            ini_set('default_socket_timeout', $socketTime);
        }

        return $res;
    }
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

#### 获取今日开始于结束时间戳

```php
function today()
	{
		$begin = strtotime('today');
		$end = strtotime('tomorrow');
		return [$begin,$end-1];
	}
```





## 文件

#### 读写数据

```php
// 普通读取
function read1($filename)
{
    $content = [];
    $fp =fopen($filename, 'rb');
    while (!feof($fp)) {
        $content[] = trim(fgets($fp));  // 读取一行
    }
    fclose($fp);
    return $content;
}
// 迭代器方式读取
function read2($filename)
{
    $fp =fopen($filename, 'rb');
    while (!feof($fp)) {
        yield trim(fgets($fp));  // 读取一行
    }
    fclose($fp);
}


// 更多读取,使用stream_copy_to_stream, 中间可以使用过滤器,进行数据的压缩
$filename = '0325.txt';

$filename2 = '8.txt';

// 文件转存
//file_put_contents($filename2, file_get_contents($filename));  // 774448
$fp1 = fopen($filename, 'r');
$fp2 = fopen($filename2, 'w');

$bytes = stream_copy_to_stream($fp1, $fp2);
var_dump($bytes);

//$filename11 = '0325.deflate';
$filename11 = '0325.zip';
$handler1 = fopen('php://filter/zlib.deflate/resource=' . $filename, 'r');
$handler2 = fopen($filename11, 'w');
stream_copy_to_stream($handler1, $handler2);  // 1114088


// 将文件进行压缩
$content = file_get_contents('php://filter/zlib.inflate/resource='.$filename11);
var_dump($content);
```

#### 读取文件某行数据

```php
function readLine($file, $line_num, $delimiter="\n")
{
    /*** set the counter to one ***/
    $i = 1;

    /*** open the file for reading ***/
    $fp = fopen( $file, 'r' );

    /*** loop over the file pointer ***/
    while ( !feof ( $fp) )
    {
        /*** read the line into a buffer ***/
        $buffer = stream_get_line( $fp, 1024, $delimiter );
        /*** if we are at the right line number ***/
        if( $i == $line_num )
        {
            /*** return the line that is currently in the buffer ***/
            return $buffer;
        }
        /*** increment the line counter ***/
        $i++;
        /*** clear the buffer ***/
        $buffer = '';
    }
    return false;
}


function readLine( $file, $line_number )
{
        /*** read the file into the iterator ***/
        $file_obj = new SplFileObject( $file );

        /*** seek to the line number ***/
        $file_obj->seek( $line_number );

        /*** return the current line ***/
        return $file_obj->current();
}
```









#### 格式化文件大小

```php
function formatSize($fileSize)
{
    $sizes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB'];
    for ($i = 0; $fileSize > 1024 && $i < 5; $i++) {
        $fileSize /= 1024;
    }
    return round($fileSize, 2).''. $sizes[$i];
}
```

#### 统计目录大小

```php
function directorySize($directory)
{
    $size = 0;
    foreach(new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory)) as $file)
    {
        $size += $file->getSize();
    }
    return $size;
}
```





#### 获取文件扩展名

```php
function getFileExt1($filename)
{
    $res = explode('.', $filename);
    return end($res);
}

function getFileExt2($filename)
{
    return substr(strrchr($filename, '.'), 1);
}

function getFileExt3($filename)
{
    $pathinfo = pathinfo($filename);
    return $pathinfo['extension'];
}
```



#### 获取文件名称唯一

```php
function generateFileId($file, $useFileName=false, $prefix="")
{
    if( !empty($file) ){
        if( !file_exists($file) )   return;
        if( !$useFileName ){
            $fileName = hash_hmac('md5',microtime(true).sha1_file($file),true );
        }else{
            $fileName = pathinfo($file,PATHINFO_FILENAME);
        }
        $fileName = $prefix.$fileName;
    }else{
        $fileName = hash_hmac('md5',sha1(uniqid(microtime(true),true).mt_rand()),true );
    }

    return $fileName;
}

// 生成文件ID
$filePath = 'test1.txt';
var_dump(generateFileId($filePath));
var_dump(generateFileId($filePath, true, 'cyd_'));
```



#### 查看某个目录下的所有文件名称

```php
function listFiles($directory)
{
    // 创建一个递归目录迭代器
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory));

    // 遍历所有文件
    foreach ($iterator as $file) {
        // 检查是否是文件（排除目录）
        if ($file->isFile()) {
            // 输出文件名称（可以根据需要处理路径）  
            echo $file->getPathname() . PHP_EOL;
        }
    }
}

// 设定要查看的目录
$targetDirectory = './';
listFiles($targetDirectory);
```









#### 获取二进制流的文件类型

```php
/**
     * 获取二进制流的文件类型
     * @param  String $stream 二进制流
     * @return String $type   文件类型
     */
    function getStreamType($stream)
    {
        if( empty($stream) ) return;
        $bin = substr($stream, 0,2);
        $code = @unpack('C2chars', $bin); //将二进制转化为十进制
        $code = intval($code['chars1'].$code['chars2']);

        $map = [
            255216  =>  'jpg',
            13780   =>  'png',
            8297    =>  'rar',
            8273    =>  'wav',
            7798    =>  'exe',
            7784    =>  'midi',
            7368    =>  'mp3',
            7173    =>  'gif',
            6677    =>  'bmp',
            0       =>  'mp4',
        ];

        return array_key_exists($code, $map) ? $map[$code] : 'unknow';
    }

$imgPath = './test.jpg';
$content = file_get_contents($imgPath);
var_dump(getStreamType($content));
```



#### 图片转base64

```php
function imgToBase64($img_file) {
    $img_base64 = '';
    if (file_exists($img_file)) {
        $img_info = getimagesize($img_file);
        if ($img_info[2] === 2 || $img_info[2] === 3) {
            $fp = fopen($img_file, "r");
            if ($fp) {
                $filesize = filesize($img_file);
                $content = fread($fp, $filesize);
                $img_base64 = chunk_split(base64_encode($content));
            }
            fclose($fp);
        }
    }
    return $img_base64;
}
```

#### 图片下载

```php
/**
 * 强制下载图片
 * @param  string $file     图片路径
 * @param  string $fileName 图片名称
 */
function downloadFile($file,$fileName){ 
	header('Pragma: public'); // required 
	header('Expires: 0'); // no cache 
	header('Cache-Control: must-revalidate, post-check=0, pre-check=0'); 
	header('Cache-Control: private',false); 
	header('Content-Type: application/force-download'); //强制下载
	header('Content-Disposition: attachment; filename="'.basename($fileName).'"'); 
	header('Content-Transfer-Encoding: binary'); 
	header('Connection: close'); 
	readfile($file); // push it out 
	exit(); 
}
```







## XML

#### 编码与解码

```php
function xml_encode($data, $encoding='utf-8', $root='root') {
	$xml = '<?xml version="1.0" encoding="' . $encoding . '"?>';
	$xml.= '<' . $root . '>';
	$xml.= data_to_xml($data);
	$xml.= '</' . $root . '>';
	return $xml;
}

function data_to_xml($data) {
	$xml = '';
	foreach ($data as $key => $val) {
		is_numeric($key) && $key = "item id=\"$key\"";
		$xml.="<$key>";
		$xml.= ( is_array($val) || is_object($val)) ? data_to_xml($val) : $val;
		list($key, ) = explode(' ', $key);
		$xml.="</$key>";
	}
	return $xml;
}
```



## 数据

#### 导出CSV格式的文件

```php
function exportCsv($filename, $data)
{
    set_time_limit(0);
    ini_set('memory_limit', '512M');

    // $output = fopen('php://output', 'w');
    $output = fopen("{$filename}.csv", 'w');

    //告诉浏览器这个是一个csv文件  
    header("Content-Type: application/csv;charset=utf-8");
    header("Content-Disposition: attachment; filename=$filename.csv");
    // header('Cache-Control:must-revalidate,post-check=0,pre-check=0');
    // header('Expires:0');
    // header('Pragma:public');
    //输出表头 
    $table_head = array('ID','名称');
    fputcsv($output, $table_head);
    //输出每一行数据到文件中  
    foreach ($data as $v) {
        //输出内容  
        fputcsv($output, array_values($v));
    }

    fclose($output);
}

// 下载CSV文件
function exportToCsv($filename, $tileArray=[], $dataArray=[]){
    ini_set('memory_limit','512M');
    ini_set('max_execution_time',0);
    ob_end_clean();
    ob_start();
    header("Content-Type: text/csv");
    header("Content-Disposition:filename=".$filename);
    $fp=fopen('php://output','w');
    fwrite($fp, chr(0xEF).chr(0xBB).chr(0xBF));//转码 防止乱码(比如微信昵称(乱七八糟的))
    fputcsv($fp,$tileArray);
    $index = 0;
    foreach ($dataArray as $item) {
        if($index==1000){
            $index=0;
            ob_flush();
            flush();
        }
        $index++;
        fputcsv($fp,$item);
    }

    ob_flush();
    flush();
    ob_end_clean();
}

```





## 正则

#### 从文章中获取所有图片

```php
function imgs($string){
    //preg_match_all函数进行全局正则表达式匹配。
//     $param1 = "/<img([^>]*)\s*src=('|\")([^'\"]+)('|\")/";  //带引号
//     $param2 = "/<img([^>]*)\ssrc=([^\s>]+)/";               //不带引号
//    $param3 = '/<img.*?src=[\'|\"](.*?(?:[\.gif|\.jpg]))[\'|\"].*?[\/]? >/i';
    $param3 = '/<img.*?src=[\'|\"](.*?)[\'|\"].*?[\/]?>/i'; 
    //这个获取图片的全部标签
    preg_match_all($param3,$string,$matches);//不带引号
    
    return $matches[0];
}
```



## 缓存

### Session

```php
// 获取,设置,删除
function session($name,$val=''){
	if($val===''){//get
		if(!isset($_SESSION[$name]))return false;
		return  $_SESSION[$name];
	}else if($val===null){//del
       unset( $_SESSION[$name]);
       return null;
	}else{//set
		$_SESSION[$name]=$val;
		return true;
	}
	return false;
}
```

### Redis

#### 分布式锁

```php
/**
 * 获取Redis分布式锁
 *
 * @param $lockKey
 * @return bool
 */function getRedisDistributedLock(string $lockKey) : bool{
    $lockTimeout = 2000;// 锁的超时时间2000毫秒
    $now = intval(microtime(true) * 1000);
    $lockExpireTime = $now + $lockTimeout;
    $lockResult = Redis::setnx($lockKey, $lockExpireTime);

    if ($lockResult) {
        // 当前进程设置锁成功
        return true;
    } else {
        $oldLockExpireTime = Redis::get($lockKey);
        if ($now > $oldLockExpireTime && $oldLockExpireTime == Redis::getset($lockKey, $lockExpireTime)) {
            return true;
        }
    }

    return false;
}


/**
 * 串行执行程序
 *
 * @param string $lockKey Key for lock
 * @param Closure $closure 获得锁后进程要执行的闭包
 * @return mixed
 */function serialProcessing(string $lockKey, Closure $closure){
    if (getRedisDistributedLock($lockKey)) {
        $result = $closure();
        $now = intval(microtime(true) * 1000);
        if ($now < Redis::get($lockKey)) {
            Redis::del($lockKey);   
        }
    } else {
        // 延迟200毫秒再执行
        usleep(200 * 1000);
        return serialProcessing($lockKey, $closure);
    }

    return $result;
}
```











## Server&Header

#### 跨域设置

```php
function set_cors_header(){
        $origin=@$_SERVER['HTTP_ORIGIN'];
        $request_method = $_SERVER['REQUEST_METHOD'];

        if ($request_method === 'OPTIONS') {
            header('Access-Control-Allow-Origin:'.$origin);
            header('Access-Control-Allow-Credentials:true');
            header('Access-Control-Allow-Methods:GET, POST, OPTIONS');
            header('Access-Control-Allow-Headers:'.$_SERVER['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']);

            header('Access-Control-Max-Age:1728000');
            header('Content-Type:text/plain charset=UTF-8');
            header('Content-Length: 0',true);

            header('status: 204');
            header('HTTP/1.0 204 No Content');
        }

        if ($request_method === 'POST') {
            header('Access-Control-Allow-Origin:'.$origin);
            header('Access-Control-Allow-Credentials:true');
            header('Access-Control-Allow-Methods:GET, POST, OPTIONS');
        }

        if ($request_method === 'GET') {
            header('Access-Control-Allow-Origin:'.$origin);
            header('Access-Control-Allow-Credentials:true');
            header('Access-Control-Allow-Methods:GET, POST, OPTIONS');
        }
    }
```





## 加解密&编码解码

#### base64变种

```php
function base64url_encode(string $data): string 
{
 return rtrim(strtr(base64_encode($data),'+/','-_'),'=');
}

function base64url_decode(string $data): string 
{
 return base64_decode(str_pad(strtr($data,'-_','+/'),strlen($data) %4,'=',STR_PAD_RIGHT));
}


# 编码
function b64encode( $string ) {
        $data = base64_encode( $string );
        $data = str_replace( array ( '+' , '/' , '=' ), array ( '-' , '_' , '' ), $data );
        return $data;
    }

# 解码

function b64decode( $string ) {
        $data = str_replace( array ( '-' , '_' ), array ( '+' , '/' ), $string );
        $mod4 = strlen( $data ) % 4;
        if ( $mod4 ) {
            $data .= substr( '====', $mod4 );
        }
        return base64_decode( $data );
}

```

#### url编码与解码

```php
    /**
     * Decode a string with URL-safe Base64.
     *
     * @param string $input A Base64 encoded string
     *
     * @return string A decoded string
     */
    public static function urlsafeB64Decode($input)
    {
        $remainder = strlen($input) % 4;
        if ($remainder) {
            $padlen = 4 - $remainder;
            $input .= str_repeat('=', $padlen);
        }
        return base64_decode(strtr($input, '-_', '+/'));
    }

    /**
     * Encode a string with URL-safe Base64.
     *
     * @param string $input The string you want encoded
     *
     * @return string The base64 encode of what you passed in
     */
    public static function urlsafeB64Encode($input)
    {
        return str_replace('=', '', strtr(base64_encode($input), '+/', '-_'));
    }
```





#### 加解密算法

```php
/**
 * 加解密算法(可用于cookie值)
 * @param string $string 数据字符串
 * @param string $key 盐值
 * @param string $operate ENCODE-加密 DECODE-解密
 * @param $expiry
 * @return false|string
 */
function authcode($string, $key, $operate='ENCODE', $expiry=0)
{
    $ckey_length = 4;

    $key = md5($key);

    $keya = md5(substr($key, 0, 16));
    $keyb = md5(substr($key, 16, 16));
    $keyc = $operate == 'DECODE' ? substr($string, 0, $ckey_length) : substr(md5(microtime()), -$ckey_length);

    $cryptkey = $keya . md5($keya . $keyc);
    $key_length = strlen($cryptkey);

    $string = $operate == 'DECODE' ? base64_decode(strtr(substr($string, $ckey_length), '-_', '+/')) : sprintf('%010d', $expiry ? $expiry + time() : 0) . substr(md5($string . $keyb), 0, 16) . $string;
    $string_length = strlen($string);

    $result = '';
    $box = range(0, 255);

    $rndkey = array();
    for ($i = 0; $i <= 255; $i++)
    {
        $rndkey[$i] = ord($cryptkey[$i % $key_length]);
    }

    for ($j = $i = 0; $i < 256; $i++)
    {
        $j = ($j + $box[$i] + $rndkey[$i]) % 256;

        $tmp = $box[$i];
        $box[$i] = $box[$j];
        $box[$j] = $tmp;
    }

    for ($i = 0; $i < $string_length; $i++)
    {
        $result .= chr(ord($string[$i]) ^ ($box[$i]));
    }

    if ($operate == 'DECODE')
    {
        if ((substr($result, 0, 10) == 0 || substr($result, 0, 10) - time() > 0) && substr($result, 10, 16) == substr(md5(substr($result, 26) . $keyb), 0, 16))
            return substr($result, 26);
        else
            return '';
    }
    else
    {
        return $keyc . rtrim(strtr(base64_encode($result), '+/', '-_'), '=');
    }
}

$string = 'lanlang';
$key = '123456';
$encryptData = authcode($string, $key);
var_dump('加密后数据:', $encryptData);
var_dump('解密后数据:', authcode($encryptData, $key, 'DECODE'));
```

#### 字符串双向加解密

```php
/**
 * 加密数据方法
 * @param String $data
 * @return String
 * @author shenpeng
 */
function encrypt($data)
{
    if (empty($data))	return $data;
    $length = strlen($data);
    $middle = (int)ceil($length/2);
    $repalcePos = 9;
    $step = (int)ceil($length*(1/4));
    //每多少个替换一次
    for($i = 0;$i<$length;$i=$i+$step){
        $temp = $data[($i+$repalcePos)%$length];
        //每次跟哪个替换
        $data[($i+$repalcePos)%$length] = $data[$i];
        $data[$i] = $temp;
    }
    $part1 = substr($data,0,$middle);
    $part2 = substr($data,$middle);
    $data = strrev($part2).strrev($part1);
    return $data;
}
/**
 * 解密数据方法
 * @param String $data
 * @return String
 * @author shenpeng
 */
function decrypt($data)
{
    if (empty($data))	return $data;
    $length = strlen($data);
    $middle = (int)ceil($length/2);
    $part1 = substr($data,0,$middle);
    $part2 = substr($data,$middle);
    $data = strrev($part2).strrev($part1);
    $repalcePos = 9;
    //每多少个替换一次
    $step = (int)ceil($length*(1/4));
    $startPos = $length-1-(($length-1)%$step);

    for($i =$startPos;$i>=0;$i=$i-$step){
        $temp = $data[($i+$repalcePos)%$length];
        //每次跟哪个替换
        $data[($i+$repalcePos)%$length] = $data[$i];
        $data[$i] = $temp;
    }
    return $data;
}
```

#### 加解密1

```php
// 加解密数据
    function key_encryption($id, $decrypt=false)
    {
        if($decrypt)
        {
            //解密
            return bzdecompress(base64_decode(str_pad(strtr($id, '-_', '+/'), strlen($id) % 4, '=', STR_PAD_RIGHT)));
        }else{
            //加密
            return rtrim(strtr(base64_encode(bzcompress($id)), '+/', '-_'), '=');
        }
    }
```

#### 加解密2

```php

	/**
	 * 加密字符串
	 * 
	 * @param decStr 需要加密的串
	 * @param strKey KEY
	 * 
	 * @return 
	 */
	private static function encrypt($decStr, $strKey)
	{
		return base64_encode(mcrypt_encrypt(MCRYPT_DES, $strKey, $decStr, MCRYPT_MODE_CBC,$strKey));
	}

	/**
	 * 解密字符串
	 * 
	 * @param encStr 需要解密的串
	 * @param strKey KEY
	 * 
	 * @return 
	 */
	private static function decrypt($encStr, $strKey)
	{
		$encStr = base64_decode(str_replace(' ','+',$encStr));
        return mcrypt_decrypt(MCRYPT_DES, $strKey, $encStr, MCRYPT_MODE_CBC,$strKey);
	}
```

#### 加解密3

```php
//加密函数
function lock_url($txt,$key='xingxing'){  
    $txt = $txt.$key;  
    $chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-=+";  
    $nh = rand(0,64);  
    $ch = $chars[$nh];  
    $mdKey = md5($key.$ch);  
    $mdKey = substr($mdKey,$nh%8, $nh%8+7);  
    $txt = base64_encode($txt);  
    $tmp = '';  
    $i=0;$j=0;$k = 0;  
    for ($i=0; $i<strlen($txt); $i++) {  
        $k = $k == strlen($mdKey) ? 0 : $k;  
        $j = ($nh+strpos($chars,$txt[$i])+ord($mdKey[$k++]))%64;  
        $tmp .= $chars[$j];  
    }  
    return urlencode(base64_encode($ch.$tmp));  
}  
//解密函数  
function unlock_url($txt,$key='xingxing'){  
    $txt = base64_decode(urldecode($txt));  
    $chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-=+";  
    $ch = $txt[0];  
    $nh = strpos($chars,$ch);  
    $mdKey = md5($key.$ch);  
    $mdKey = substr($mdKey,$nh%8, $nh%8+7);  
    $txt = substr($txt,1);  
    $tmp = '';  
    $i=0;$j=0; $k = 0;  
    for ($i=0; $i<strlen($txt); $i++) {  
        $k = $k == strlen($mdKey) ? 0 : $k;  
        $j = strpos($chars,$txt[$i])-$nh - ord($mdKey[$k++]);  
        while ($j<0) $j+=64;  
        $tmp .= $chars[$j];  
    }  
    return trim(base64_decode($tmp),$key);  
}

```







## 系统函数

- base_convert: 在任意进制之间转换 





## 助手

#### 友好打印

```php
function dump( $var, $echo = true, $label = null, $strict = true ) {
        $label = ( $label === null ) ? '' : rtrim( $label ) . ' ';
        if ( ! $strict ) {
            if ( ini_get( 'html_errors' ) ) {
                $output = print_r( $var, true );
                $output = "<pre>" . $label . htmlspecialchars( $output, ENT_QUOTES ) . "</pre>";
            } else {
                $output = $label . print_r( $var, true );
            }
        } else {
            ob_start();
            var_dump( $var );
            $output = ob_get_clean();
            if ( ! extension_loaded( 'xdebug' ) ) {
                $output = preg_replace( "/\]\=\>\n(\s+)/m", "] => ", $output );
                $output = '<pre>' . $label . htmlspecialchars( $output, ENT_QUOTES ) . '</pre>';
            }
        }
        if ( $echo ) {
            echo $output;
            return null;
        } else
            return $output;
    }
```







## 其他

#### 多分类数据存储与解析

```php
// 存储的时候(1 << $j1 + 1 << $j2 ...)
function getConvertTexts() {
    //id 不能超过31 for ($i=0;$i<33;$i++) echo ( 1<< $i ) . '<br>';    32位 整型数字长度的限制
    return  [
        20=>'周边游',21=>'私家定制',18=>'线路',17=>'小团',15=>'新品',0=>'特色体验',1=>'精品酒店',8=>'品牌酒店',
        2=>'海外自由行',3=>'国内度假',9=>'精美民宿',10=>'独家',16=>'特卖产品',12=>'酒店民宿',13=>'地方风味',
        14=>'度假线路',6=>'双11活动',7=>'热门海岛',11=>'景区门票',4=>'海外酒店',22=>'国内酒店'
    ];
}
// 根据分类将类型进行解析
function convert_style( $style, array $texts = [] ) {
    if ( empty($texts) ) {
        $texts = getConvertTexts();
    }

    $tags = [];
    if ( is_numeric($style) && $style > 0 ) {
        for ( $i = 0; $i < 31; $i++ ) {
            $num = (1 << $i);
            if ( isset($texts[$i]) && ( $num & $style ) ) {
                $tags[] = $texts[$i];
            }
        }

    }
    return $tags;
}
```



#### 抽奖算法

```php
$signRate = array(
    '1' => 30,
    '2' => 25,
    '3' => 20,
    '4' => 15,
    '5' => 10
);
// 随机抽奖
function getRand($proArr)
{
    $result = '';
    // 概率数组的总概率精度
    $proSum = array_sum($proArr);
    // 概率数组循环
    foreach ($proArr as $key => $proCur) {
        $randNum = mt_rand(1, $proSum); // 抽取随机数
        if ($randNum <= $proCur) {
            $result = $key; // 得出结果
            break;
        } else {
            $proSum -= $proCur;
        }
    }
    unset($proArr);
    return $result;
}
```

#### 下载Excel大文件

```sql
articleAccessLog($timeStart='20181201', $timeEnd='20181210');

function articleAccessLog($timeStart, $timeEnd)
{
    set_time_limit(0);

    $columns = [
        '文章ID'
    ];
    $fileName = '用户日志' . $timeStart .'_'. $timeEnd . '.xls';
    //设置好告诉浏览器要下载excel文件的headers
    header('Content-Description: File Transfer');
    header('Content-Type: application/vnd.ms-excel');
    header('Content-Disposition: attachment; filename="'. $fileName .'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');//强制页面不缓存
    header('Pragma: public');

    $fp = fopen('php://output', 'a');//打开output流
    mb_convert_variables('GBK', 'UTF-8', $columns);
    fputcsv($fp, $columns);//将数据格式化为CSV格式并写入到output流中
    $accessNum = '1000000';//从数据库获取总量，假设是一百万
    $perSize = 1000;//每次查询的条数
    $pages   = ceil($accessNum / $perSize);
    for($i = 1; $i <= $pages; $i++) {
        $accessLog = range($i+($i-1)*$perSize,$i*$perSize);
        foreach($accessLog as $access) {
            $rowData = [
                $access //每一行的数据
            ];
            mb_convert_variables('GBK', 'UTF-8', $rowData);
            fputcsv($fp, $rowData);
        }
        unset($accessLog);//释放变量的内存
        //刷新输出缓冲到浏览器
        ob_flush();
        flush();//必须同时使用 ob_flush() 和flush() 函数来刷新输出缓冲。
    }
    fclose($fp);
    exit();
}
```





#### 接口的数据加密

```php
// 1.一般传递的额外参数
	nonce: 随机数
    ts: 时间戳(检查时效性)
    sign: 签名(例如:加密方式 md5(POST参数（升序排序，除key sign参数除外） + 用户密钥))
    key/appId: 用户访问标识
// 2.设置Ip白名单
```



#### 分库分表

```php
function getHash(&$key, $n = 64) {
    $hash = crc32($key) >> 16 & 0xffff;
    return sprintf("%02s", $hash % $n);
}


public function getStringHash($string, $tab_count)
{
        $unsign = sprintf('%u', crc32($string));
        if ($unsign > 2147483647)  // sprintf u for 64 & 32 bit
        {
            $unsign -= 4294967296;
        }
        return abs($unsign) % $tab_count;
}
```









