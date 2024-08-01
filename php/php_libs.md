# php常用类库

## 验证码

```php
 class YzCode {  

        private $charset = 'abcdefghkmnprstuvwxyzABCDEFGHKMNPRSTUVWXYZ23456789';    //随机因子  
        private $code;                            //验证码  
        private $codelen = 4;                    //验证码长度  
        private $width = 130;                    //宽度  
        private $height = 50;                    //高度  
        private $img;                                //图形资源句柄  
        private $font;                                //指定的字体  
        private $fontsize = 20;                //指定字体大小  
        private $fontcolor;                        //指定字体颜色  
      
     
        //构造方法初始化  
        public function __construct() {  
            #echo 'web/static/font/elephant.ttf';exit;
            $this->font = APPLICATION_PATH .'/public/rsc/fonts/elephant.ttf';  
        }  

      
        //生成随机码  
        private function createCode() {  
            $_len = strlen($this->charset)-1;  
            for ($i=0;$i<$this->codelen;$i++) {  
                $this->code .= $this->charset[mt_rand(0,$_len)];  
            }  
        }

      
      
        //生成背景  
        private function createBg() {  
            $this->img = imagecreatetruecolor($this->width, $this->height);  
            $color = imagecolorallocate($this->img, mt_rand(157,255), mt_rand(157,255), mt_rand(157,255));  
            imagefilledrectangle($this->img,0,$this->height,$this->width,0,$color);  
        }  
      
      
        //生成文字  
        private function createFont() {      
            $_x = $this->width / $this->codelen;  
            for ($i=0;$i<$this->codelen;$i++) {  
                $this->fontcolor = imagecolorallocate($this->img,mt_rand(0,156),mt_rand(0,156),mt_rand(0,156));  
                imagettftext($this->img,$this->fontsize,mt_rand(-30,30),$_x*$i+mt_rand(1,5),$this->height / 1.4,$this->fontcolor,$this->font,$this->code[$i]);  
            }  
        }  
      
      
        //生成线条、雪花  
        private function createLine() {  
            for ($i=0;$i<6;$i++) {  
                $color = imagecolorallocate($this->img,mt_rand(0,156),mt_rand(0,156),mt_rand(0,156));  
                imageline($this->img,mt_rand(0,$this->width),mt_rand(0,$this->height),mt_rand(0,$this->width),mt_rand(0,$this->height),$color);  
            }  
            for ($i=0;$i<100;$i++) {  
                $color = imagecolorallocate($this->img,mt_rand(200,255),mt_rand(200,255),mt_rand(200,255));  
                imagestring($this->img,mt_rand(1,5),mt_rand(0,$this->width),mt_rand(0,$this->height),'*',$color);  
            }  
        }  
      
      
        //输出  
        private function outPut() {  
            header('Content-type:image/png');  
            imagepng($this->img);  
            imagedestroy($this->img);  
        }  
      
      
        //对外生成  
        public function doimg() {  
            $this->createBg();  
            $this->createCode();  
            $this->createLine();  
            $this->createFont();  
            $this->outPut();  
        }  
      
      
        //获取验证码  
        public function getCode() {  
            return strtolower($this->code);  
        }  

    }

$_vc = new YzCode();      //实例化一个对象  
$_vc->doimg();             
$_SESSION['verifyCode'] = $_vc->getCode(); 
```

## 网络请求

```php
<?php

class RestRequest
{
	protected $url;
	protected $verb;
	protected $requestBody;
	protected $requestLength;
	protected $username;
	protected $password;
	protected $acceptType;
	protected $responseBody;
	protected $responseInfo;
	
	public function __construct ($url = null, $verb = 'GET', $requestBody = null)
	{
		$this->url				= $url;
		$this->verb				= $verb;
		$this->requestBody		= $requestBody;
		$this->requestLength	= 0;
		$this->username			= null;
		$this->password			= null;
		$this->acceptType		= 'application/json';
		$this->responseBody		= null;
		$this->responseInfo		= null;
		
		if ($this->requestBody !== null)
		{
			$this->buildPostBody();
		}
	}
	
	public function flush ()
	{
		$this->requestBody		= null;
		$this->requestLength	= 0;
		$this->verb				= 'GET';
		$this->responseBody		= null;
		$this->responseInfo		= null;
	}
	
	public function execute ()
	{
		$ch = curl_init();
		$this->setAuth($ch);
		
		try
		{
			switch (strtoupper($this->verb))
			{
				case 'GET':
					$this->executeGet($ch);
					break;
				case 'POST':
					$this->executePost($ch);
					break;
				case 'PUT':
					$this->executePut($ch);
					break;
				case 'DELETE':
					$this->executeDelete($ch);
					break;
				default:
					throw new InvalidArgumentException('Current verb (' . $this->verb . ') is an invalid REST verb.');
			}
		}
		catch (InvalidArgumentException $e)
		{
			curl_close($ch);
			throw $e;
		}
		catch (Exception $e)
		{
			curl_close($ch);
			throw $e;
		}
		
	}
	
	public function buildPostBody ($data = null)
	{
		$data = ($data !== null) ? $data : $this->requestBody;
		
		if (!is_array($data))
		{
			throw new InvalidArgumentException('Invalid data input for postBody.  Array expected');
		}
		
		$data = http_build_query($data, '', '&');
		$this->requestBody = $data;
	}
	
	protected function executeGet ($ch)
	{		
		$this->doExecute($ch);	
	}
	
	protected function executePost ($ch)
	{
		if (!is_string($this->requestBody))
		{
			$this->buildPostBody();
		}
		
		curl_setopt($ch, CURLOPT_POSTFIELDS, $this->requestBody);
		curl_setopt($ch, CURLOPT_POST, 1);
		
		$this->doExecute($ch);	
	}
	
	protected function executePut ($ch)
	{
		if (!is_string($this->requestBody))
		{
			$this->buildPostBody();
		}
		
		$this->requestLength = strlen($this->requestBody);
		
		$fh = fopen('php://memory', 'rw');
		fwrite($fh, $this->requestBody);
		rewind($fh);
		
		curl_setopt($ch, CURLOPT_INFILE, $fh);
		curl_setopt($ch, CURLOPT_INFILESIZE, $this->requestLength);
		curl_setopt($ch, CURLOPT_PUT, true);
		
		$this->doExecute($ch);
		
		fclose($fh);
	}
	
	protected function executeDelete ($ch)
	{
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'DELETE');
		
		$this->doExecute($ch);
	}
	
	protected function doExecute (&$curlHandle)
	{
		$this->setCurlOpts($curlHandle);
		$this->responseBody = curl_exec($curlHandle);
		$this->responseInfo	= curl_getinfo($curlHandle);
		
		curl_close($curlHandle);
	}
	
	protected function setCurlOpts (&$curlHandle)
	{
		curl_setopt($curlHandle, CURLOPT_TIMEOUT, 10);
		curl_setopt($curlHandle, CURLOPT_URL, $this->url);
		curl_setopt($curlHandle, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($curlHandle, CURLOPT_HTTPHEADER, array ('Accept: ' . $this->acceptType));
	}
	
	protected function setAuth (&$curlHandle)
	{
		if ($this->username !== null && $this->password !== null)
		{
			curl_setopt($curlHandle, CURLOPT_HTTPAUTH, CURLAUTH_DIGEST);
			curl_setopt($curlHandle, CURLOPT_USERPWD, $this->username . ':' . $this->password);
		}
	}
	
	public function getAcceptType ()
	{
		return $this->acceptType;
	} 
	
	public function setAcceptType ($acceptType)
	{
		$this->acceptType = $acceptType;
	} 
	
	public function getPassword ()
	{
		return $this->password;
	} 
	
	public function setPassword ($password)
	{
		$this->password = $password;
	} 
	
	public function getResponseBody ()
	{
		return $this->responseBody;
	} 
	
	public function getResponseInfo ()
	{
		return $this->responseInfo;
	} 
	
	public function getUrl ()
	{
		return $this->url;
	} 
	
	public function setUrl ($url)
	{
		$this->url = $url;
	} 
	
	public function getUsername ()
	{
		return $this->username;
	} 
	
	public function setUsername ($username)
	{
		$this->username = $username;
	} 
	
	public function getVerb ()
	{
		return $this->verb;
	} 
	
	public function setVerb ($verb)
	{
		$this->verb = $verb;
	} 
}

// 使用
$rs = new RestRequest($url,'POST',$requestBody);
$rs->execute();
$result = $rs->getResponseBody();
```









## 文件上传

```php
/**
     * FileUpload.class.php
     * @Description 多文件上传类
     * Time: 2013-10-3
     *        include "FileUpload.class.php";
     *      $up=new FileUpload(array('savepath'=>'./mytest/'));
     *      $up->uploadFile('userfile');  //userfile 为input框的name值 多文件时input 的name值要有中括号: name="userfile[]" 没有中括号只能上传第一个文件
     *      echo $up->getErrorMsg();  //得到错误信息
     *         
     * 基本功能有 都以参数形式传入构造函数
     *         指定上传文件格式 [array] allowtype 
     *         指定文件大小     [int] maxsize
     *         
     * 实例1 上传头像到指定目录 并以随即名保存 文件名长度为20(默认为20)
     *         $up = new FileUpload(array('savepath'=>'./avatar/', 'israndname'=>true, 'newfilenamelength'=>20));
     * 实例2 上传头像到指定目录 并且用用户id作为文件名 如上传 photo.png 保存为 2.png
     *         $up = new FileUpload(array('savepath'=>'./avatar/', 'israndname'=>false, 'givenfilename'=>2));
     * 实例3 上传头像到指定目录 在目录下以日期为单位建立子目录保存头像
     *         $up = new FileUpload(array('savepath'=>'./avatar/', 'subdirpattern'=>'Y/m' , 'israndname'=>false, 'givenfilename'=>2));
     *         以上生成目录为 './avatar/2013/10'
     */
    class Util_Upload_FileUpload {
        private $name = 'name';
        private $type = 'type';
        private $tmp_name = 'tmp_name';
        private $error = 'error';
        private $size = 'size';
        // 构造方法用到的字段
        private $savepath = '';  //指定上传文件保存的路径
        private $subdirpattern = '';  // 结合savepath使用 为空表示不添加子目录,不为空 比如 'Y/m' 表示 2011/01 那么保存路径就是 $savepath  . '/2011/01'
        private $allowtype = array('gif', 'jpg', 'png');
        private $maxsize = 204800; //Byte 200K
        private $israndname = true;  //是否随机重命名 true false不随机 使用原文件名
        private $givenfilename = '';  //使用给定的文件名 配合 israndname 使用
        private $ignoreemptyfile = true;  //是否忽略没有上传文件的文本域
        private $newfilenamelength = 20;
        
        // 本类用到的字段
        private $errorMessage = '';
        private $uploadFileArray = null;
        private $originalFileName = '';
        private $expandedName = '';
        public $newFileName = '';
        
        
        //1. 指定上传路径， 2，充许的类型， 3，限制大小， 4，是否使用随机文件名称
        //new FileUpload( array('savepath'=>'./uploads/', 'allowtype'=>array('txt','gif'), 'israndname'=>true) );
        public function __construct($args=array()) {
            foreach($args as $key => $value) {
                $key = strtolower($key);
                //查看用户参数中数组的下标是否和成员属性名相同
                //if(!in_array( $key, get_class_vars(get_class($this)) )) {
                //    continue;
                //}
                $this->setArgs($key, $value);
            }
        }
        
        private function setArgs($key, $value) {
            $this->$key = $value;
        }
        
        /**
         * 得到文件大小
         * @param int size 字节数
         */
        private function getFileSize($size) {
            $unit = 'Bytes';
            if($size < 1024) {
                return $size.$unit;
            } else if($size < pow(1024, 2)) {
                $unit = 'KB';
                $size = round($size / 1024, 2);
            } else if($size < pow(1024, 3)) {
                $unit = 'MB';
                $size = round($size / pow(1024, 2), 2);
            } else if($size < pow(1024, 4)) {
                $unit = 'GB';
                $size = round($size / pow(1024, 3), 2);
            } else {
                $unit = 'TB';
                $size = round($size / pow(1024, 4), 2);
            }
            
            return $size.$unit;
        }
        
        /**
         * 得到一个数组的键组成的数组
         */
        private function myArray_keys(& $arr) {
            $returnArr = array();
            foreach($arr as $key => $val) {
                $returnArr[] = $key;
            }
            
            return $returnArr;
        }
    /* 没排序时
    Array
    (
        [f1] => Array
            (
                [name] => Array
                    (
                        [0] => Winter.jpg
                    )
                // 凡是加了[] 这里的name格式就成了数组 这是才能支持多文件
                // 凡是不加[] 这里的name格式就是字符串 也就是只能上传第一个文件
                
                [type] => Array
                    (
                        [0] => image/jpeg
                    )
                [tmp_name] => Array
                    (
                        [0] => C:\WINDOWS\TEMP\php38D.tmp
                    )
                [error] => Array
                    (
                        [0] => 0
                    )
                [size] => Array
                    (
                        [0] => 105542
                    )
            )
    )
    */
        
        /**
         * 重新排列上传文件
         * $uploadFileArray 上传的文件的数组
         */
        private function reSortFile(& $uploadFileArray) {
            // input name没有[] 时是字符串
            // 有[] 时是数组
            $multiFlag = is_array($uploadFileArray[$this->name]) ? true : false;
            $file_arr = array();
            
            $file_num = $multiFlag ? count($uploadFileArray[$this->name]) : 1;  //计算上传的文件数
            $file_keys = $this->myArray_keys($uploadFileArray);  //得到数组,包含了name type error tmp_name size
            
            for($i=0; $i<$file_num; $i++) {
                foreach($file_keys as $value) {
                    $file_arr[$i][$value] = $multiFlag ? $uploadFileArray[$value][$i] : $uploadFileArray[$value];
                }
            }
            
            return $file_arr;
        }
        
        /**
         * 错误报告 
         * $errorno 错误号
         */
        private function setErrorMsg($errorno){
            $msg = "上传文件<font color='red'> {$this->originalFileName} </font>时出错: ";
            switch($errorno){
                case 1:
                case 2:
                    $msg .= '文件过大,无法上传';  //配置文件中的大小
                case 3:
                    $msg .= '文件只被部分上传'; break;
                case -1:
                    $msg .= '不充许的文件类型'; break;
                case -2:
                    $msg .= '文件过大,上传文件不能超过'.$this->getFileSize($this->maxsize); break;
                case -3: 
                    $msg .= '上传失败'; break;
                case -4:
                    $msg .= '建立存放上传文件目录失败,请重新指定上传目录'; break;
                case -5:
                    $msg .= '必须指定上传文件的路径'; break;
                case -6:
                    $msg .= '不是上传的文件'; break;
                default: $msg .=  "未知错误";
            }
            return $msg.'<br>';
        }
        
        /**
         * 检查有没有指定上传路径
         */
        private function emptySavePath() {
            if(empty($this->savepath)) {
                $this->errorMessage .= $this->setErrorMsg(-5);
                return true;
            }
            return false;
        }
        
        /**
         * 得到扩展名
         * $fileName 文件名
         */
        private function getExpandedName() {
            $pos = strrpos($this->originalFileName, '.');
            return substr($this->originalFileName, $pos+1);
        }
        
        /**
         * 检查文件扩展名是够合法
         */
        private function isLegalExpandedName() {
            if(in_array($this->expandedName, $this->allowtype)) {
                return true;
            }
            $this->errorMessage .= $this->setErrorMsg(-1);
            
            return false;
        }
        
        /**
         * 检查上传的文件有没有错误
         * $i 第几个文件
         */
        private function hasError($i) {
            $errorno = $this->uploadFileArray[$i][$this->error];
            if(0 == $errorno) {
                return 0; //文件正常
            } else if(4 == $errorno) {
                return 4;  //没有上传文件
            }
            $this->errorMessage .= $this->setErrorMsg($errorno);
            
            return 99;  //文件有错误
        }
        
        /**
         * 检查文件大小
         * $i 第几个文件
         */
        private function isLegalSize($i) {
            $fileSize = $this->uploadFileArray[$i][$this->size];
            if($fileSize <= $this->maxsize) {
                return true;
            }
            $this->errorMessage .= $this->setErrorMsg(-2);
            return false;
        }
        
        /**
         * 检查所给出的文件是否是通过HTTP POST上传的
         * $i 第几个文件
         */
        private function isUploadedFile($i) {
            $tmpName = $this->uploadFileArray[$i][$this->tmp_name];
            if(is_uploaded_file($tmpName)) {
                return true;
            }
            $this->errorMessage .= $this->setErrorMsg(-6);
            return false;
        }
        
        /**
         * 得到新文件名(如果用户指定不用新文件名则使用旧文件名)
         *
         */
        private function initNewFileName() {
            $str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
            $chars = $this->originalFileName;  // 有后缀 .jpg
            if($this->israndname) {
                $chars = '';
                for($i=0; $i<$this->newfilenamelength-8; $i++) {
                    $chars .= substr($str, mt_rand(0, strlen($str)-1), 1);
                }
                $chars .= date('Ymd', time());
                $chars = $chars . '.' . $this->expandedName;
            } else {
                // 给定了使用指定的名字
                if('' != $this->givenfilename) {
                    $chars = $this->givenfilename . '.' . $this->expandedName;
                }
            }
            
            return $chars;
        }
        
        /**
         * 复制文件到指定地方
         * $i 第几个文件
         */
        private function copyFile($i) {
        	$this->newFileName = $this->initNewFileName();
        
        	if(is_dir($this->savepath)) {
        		@move_uploaded_file($this->uploadFileArray[$i][$this->tmp_name], $this->savepath.iconv("UTF-8","gb2312",$this->newFileName));
        	} else {
        		die('上传目录创建失败');
        	}
        }
        
        /**
         * 检查是否有空文件
         */
        private function chkEmptyFile(& $arr) {
            $flag = 1;
            for($i = 0; $i < count($arr); $i++) {
                if(intval($arr[$i][$this->error]) == 4) {
                    $flag = 4;
                    break;
                }
            }
            
            return $flag;
        }
        
        /**
         * 初始化上传文件夹
         */
        private function initSavePath() {
            $this->savepath = rtrim($this->savepath, '/') . '/';
            !empty($this->subdirpattern) && $this->savepath = $this->savepath . date($this->subdirpattern, time()) . '/';
            
            $tmpSavePath = rtrim($this->savepath, '/');
            if(!is_dir($tmpSavePath)) {
                $dirs = explode('/', $tmpSavePath);
                $realDir = '';
                for($i = 0; $i < count($dirs); $i++) {
                    if($dirs[$i] == '') continue;
                    if($dirs[$i] == '.') {
                        $realDir .= './';
                    } else {
                        $realDir = $realDir . $dirs[$i] . '/';
                    }
                    
                    if(!is_dir($realDir))
                        mkdir($realDir);
                }
            }
        }
        
        /**
         * 开始上传文件方法
         */
        private function startUpload() {
            for($i=0; $i<count($this->uploadFileArray); $i++) {
                if(0 === $this->hasError($i)) {
                    $this->originalFileName = $this->uploadFileArray[$i][$this->name];  // aa.jpg
                    $this->expandedName = $this->getExpandedName();
                    if($this->isLegalExpandedName()) {
                        if($this->isLegalSize($i)) {
                            //if($this->isUploadedFile($i)) {
                                $this->copyFile($i);
                            //}
                        }
                    }
                }
            }
        }
        
        /**
         * 上传文件 入口
         * $fileField input框的name属性值
         */
        public function uploadFile($fileField) {
            //检查上传路径
            if(true === $this->emptySavePath()) {
                return false;
            }
            
            if(0 !== count($_FILES)) {
                //重新排列上传文件
                $this->uploadFileArray = $this->reSortFile($_FILES[$fileField]);
                
                //开始上传文件
                if( !$this->ignoreemptyfile && 4 == $this->chkEmptyFile($this->uploadFileArray) ) {
                    die('强制全部上传模式');
                    
                } else {
                    $this->initSavePath();  // 初始化上传路径
                    $this->startUpload();
                }
            }
        }
         
        /**
         * de到错误信息 
         */     
        public function getErrorMsg() {
            return $this->errorMessage;
        }
        
        public function getUploadFileName() {
            return $this->savepath.$this->newFileName;
        }
    }
```



## 布隆过滤器

#### 未使用缓存

```php

<?php
 
/**
 * Implements a Bloom Filter
 */
class BloomFilter {
    /**
     * Size of the bit array
     *
     * @var int
     */
    protected $m;
 
    /**
     * Number of hash functions
     *
     * @var int
     */
    protected $k;
 
    /**
     * Number of elements in the filter
     *
     * @var int
     */
    protected $n;
 
    /**
     * The bitset holding the filter information
     *
     * @var array
     */
    protected $bitset;
 
    /**
     * 计算最优的hash函数个数：当hash函数个数k=(ln2)*(m/n)时错误率最小
     *
     * @param int $m bit数组的宽度（bit数）
     * @param int $n 加入布隆过滤器的key的数量
     * @return int
     */
    public static function getHashCount($m, $n) {
        return ceil(($m / $n) * log(2));
    }
 
    /**
     * Construct an instance of the Bloom filter
     *
     * @param int $m bit数组的宽度（bit数） Size of the bit array
     * @param int $k hash函数的个数 Number of different hash functions to use
     */
    public function __construct($m, $k) {

        $this->m = $m;
        $this->k = $k;
        $this->n = 0;
 
        /* Initialize the bit set */
        $this->bitset = array_fill(0, $this->m - 1, false);
    }
 
    /**
     * False Positive的比率：f = (1 – e-kn/m)k   
     * Returns the probability for a false positive to occur, given the current number of items in the filter
     *
     * @return double
     */
    public function getFalsePositiveProbability() {
        $exp = (-1 * $this->k * $this->n) / $this->m;
 
        return pow(1 - exp($exp),  $this->k);
    }
 
    /**
     * Adds a new item to the filter
     *
     * @param mixed Either a string holding a single item or an array of 
     *              string holding multiple items.  In the latter case, all
     *              items are added one by one internally.
     */
    public function add($key) {
        if (is_array($key)) {
            foreach ($key as $k) {
                $this->add($k);
            }
            return;
        }
 
        $this->n++;
 
        foreach ($this->getSlots($key) as $slot) {
            $this->bitset[$slot] = true;
        }
    }
 
    /**
     * Queries the Bloom filter for an element
     *
     * If this method return FALSE, it is 100% certain that the element has
     * not been added to the filter before.  In contrast, if TRUE is returned,
     * the element *may* have been added to the filter previously.  However with
     * a probability indicated by getFalsePositiveProbability() the element has
     * not been added to the filter with contains() still returning TRUE.
     *
     * @param mixed Either a string holding a single item or an array of 
     *              strings holding multiple items.  In the latter case the
     *              method returns TRUE if the filter contains all items.
     * @return boolean
     */
    public function contains($key) {
        if (is_array($key)) {
            foreach ($key as $k) {
                if ($this->contains($k) == false) {
                    return false;
                }
            }
 
            return true;
        }
 
        foreach ($this->getSlots($key) as $slot) {
            if ($this->bitset[$slot] == false) {
                return false;
            }
        }
 
        return true;
    }
 
    /**
     * Hashes the argument to a number of positions in the bit set and returns the positions
     *
     * @param string Item
     * @return array Positions
     */
    protected function getSlots($key) {
        $slots = array();
        $hash = self::getHashCode($key);
        mt_srand($hash);
 
        for ($i = 0; $i < $this->k; $i++) {
            $slots[] = mt_rand(0, $this->m - 1);
        }
 
        return $slots;
    }
 
    /**
     * 使用CRC32产生一个32bit（位）的校验值。
     * 由于CRC32产生校验值时源数据块的每一bit（位）都会被计算，所以数据块中即使只有一位发生了变化，也会得到不同的CRC32值。
     * Generates a numeric hash for the given string
     *
     * Right now the CRC-32 algorithm is used.  Alternatively one could e.g.
     * use Adler digests or mimick the behaviour of Java's hashCode() method.
     *
     * @param string Input for which the hash should be created
     * @return int Numeric hash
     */
    protected static function getHashCode($string) {
        return crc32($string);
    }
    
}
 
 
 
$items = array("first item", "second item", "third item");
        
/* Add all items with one call to add() and make sure contains() finds
 * them all.
 */
$filter = new BloomFilter(100, BloomFilter::getHashCount(100, 3));
// var_dump($filter); exit;
$filter->add($items);
 
// var_dump($filter); exit;
$items = array("firsttem", "seconditem", "thirditem");
foreach ($items as $item) {
 var_dump(($filter->contains($item)));
}




 
/* Add all items with multiple calls to add() and make sure contains()
* finds them all.
*/
$filter = new BloomFilter(100, BloomFilter::getHashCount(100, 3));
foreach ($items as $item) {
	$filter->add($item);
}
$items = array("fir sttem", "secondit em", "thir ditem");

foreach ($items as $item) {
 var_dump(($filter->contains($item)));
}
```

#### 结合Redis使用

```php
class BloomFilterHash
{
	/**
	 * 由Justin Sobel编写的按位散列函数
	 */
	public function JSHash($string, $len = null)
	{
    	$hash = 1315423911;
    	$len || $len = strlen($string);
    	for ($i=0; $i<$len; $i++) {
    		$hash ^= (($hash << 5) + ord($string[$i]) + ($hash >> 2));
    	}
		return ($hash % 0xFFFFFFFF) & 0xFFFFFFFF;
	}

	/**
	 * 该哈希算法基于AT＆T贝尔实验室的Peter J. Weinberger的工作。
	 * Aho Sethi和Ulman编写的“编译器（原理，技术和工具）”一书建议使用采用此特定算法中的散列方法的散列函数。
	 */
	public function PJWHash($string, $len = null)
	{
		$bitsInUnsignedInt = 4 * 8; //（unsigned int）（sizeof（unsigned int）* 8）;
    	$threeQuarters = ($bitsInUnsignedInt * 3) / 4;
    	$oneEighth = $bitsInUnsignedInt / 8;
    	$highBits = 0xFFFFFFFF << (int) ($bitsInUnsignedInt - $oneEighth);
    	$hash = 0;
    	$test = 0;
    	$len || $len = strlen($string);
    	for($i=0; $i<$len; $i++) {
			$hash = ($hash << (int) ($oneEighth)) + ord($string[$i]); } $test = $hash & $highBits; if ($test != 0) { $hash = (($hash ^ ($test >> (int)($threeQuarters))) & (~$highBits));
    	}
		return ($hash % 0xFFFFFFFF) & 0xFFFFFFFF;
	}

	/**
	 * 类似于PJW Hash功能，但针对32位处理器进行了调整。它是基于UNIX的系统上的widley使用哈希函数。
	 */
	public function ELFHash($string, $len = null)
	{
		$hash = 0;
		$len || $len = strlen($string);
    	for ($i=0; $i<$len; $i++) {
        	$hash = ($hash << 4) + ord($string[$i]); $x = $hash & 0xF0000000; if ($x != 0) { $hash ^= ($x >> 24);
        	}
        	$hash &= ~$x;
    	}
		return ($hash % 0xFFFFFFFF) & 0xFFFFFFFF;
	}

	/**
	 * 这个哈希函数来自Brian Kernighan和Dennis Ritchie的书“The C Programming Language”。
	 * 它是一个简单的哈希函数，使用一组奇怪的可能种子，它们都构成了31 .... 31 ... 31等模式，它似乎与DJB哈希函数非常相似。
	 */
	public function BKDRHash($string, $len = null)
	{
    	$seed = 131;  # 31 131 1313 13131 131313 etc..
    	$hash = 0;
    	$len || $len = strlen($string);
    	for ($i=0; $i<$len; $i++) {
        	$hash = (int) (($hash * $seed) + ord($string[$i]));
    	}
		return ($hash % 0xFFFFFFFF) & 0xFFFFFFFF;
	}

	/**
	 * 这是在开源SDBM项目中使用的首选算法。
	 * 哈希函数似乎对许多不同的数据集具有良好的总体分布。它似乎适用于数据集中元素的MSB存在高差异的情况。
	 */
	public function SDBMHash($string, $len = null)
	{
		$hash = 0;
		$len || $len = strlen($string);
		for ($i=0; $i<$len; $i++) {
			$hash = (int) (ord($string[$i]) + ($hash << 6) + ($hash << 16) - $hash);
		}
		return ($hash % 0xFFFFFFFF) & 0xFFFFFFFF;
	}

	/**
	 * 由Daniel J. Bernstein教授制作的算法，首先在usenet新闻组comp.lang.c上向世界展示。
	 * 它是有史以来发布的最有效的哈希函数之一。
	 */
	public function DJBHash($string, $len = null)
	{
		$hash = 5381;
		$len || $len = strlen($string);
		for ($i=0; $i<$len; $i++) {
			$hash = (int) (($hash << 5) + $hash) + ord($string[$i]);
		}
		return ($hash % 0xFFFFFFFF) & 0xFFFFFFFF;
	}

	/**
	 * Donald E. Knuth在“计算机编程艺术第3卷”中提出的算法，主题是排序和搜索第6.4章。
	 */
	public function DEKHash($string, $len = null)
	{
		$len || $len = strlen($string);
		$hash = $len;
		for ($i=0; $i<$len; $i++) {
			$hash = (($hash << 5) ^ ($hash >> 27)) ^ ord($string[$i]);
		}
		return ($hash % 0xFFFFFFFF) & 0xFFFFFFFF;
	}

	/**
	 * 参考 http://www.isthe.com/chongo/tech/comp/fnv/
	 */
	public function FNVHash($string, $len = null)
	{
		$prime = 16777619; //32位的prime 2^24 + 2^8 + 0x93 = 16777619
		$hash = 2166136261; //32位的offset
		$len || $len = strlen($string);
		for ($i=0; $i<$len; $i++) {
			$hash = (int) ($hash * $prime) % 0xFFFFFFFF;
			$hash ^= ord($string[$i]);
		}
		return ($hash % 0xFFFFFFFF) & 0xFFFFFFFF;
	}
}





/**
 * 使用redis实现的布隆过滤器
 */
abstract class BloomFilterRedis
{
	/**
	 * 需要使用一个方法来定义bucket的名字
	 */
	protected $bucket;

	protected $hashFunction;

	public function __construct($config, $id)
	{
		if (!$this->bucket || !$this->hashFunction) {
			throw new Exception("需要定义bucket和hashFunction", 1);
		}
		$this->Hash = new BloomFilterHash;
		$this->Redis = new YourRedis; //假设这里你已经连接好了
	}

	/**
	 * 添加到集合中
	 */
	public function add($string)
	{
		$pipe = $this->Redis->multi();
		foreach ($this->hashFunction as $function) {
			$hash = $this->Hash->$function($string);
			$pipe->setBit($this->bucket, $hash, 1);
		}
		return $pipe->exec();
	}

	/**
	 * 查询是否存在, 不存在的一定不会存在, 存在有一定几率会误判
	 */
	public function exists($string)
	{
		$pipe = $this->Redis->multi();
		$len = strlen($string);
		foreach ($this->hashFunction as $function) {
			$hash = $this->Hash->$function($string, $len);
			$pipe = $pipe->getBit($this->bucket, $hash);
		}
		$res = $pipe->exec();
		foreach ($res as $bit) {
			if ($bit == 0) {
				return false;
			}
		}
		return true;
	}

}
// 上面定义的是一个抽象类，如果要使用，可以根据具体的业务来使用。比如下面是一个过滤重复内容的过滤器。

/**
 * 重复内容过滤器
 * 该布隆过滤器总位数为2^32位, 判断条数为2^30条. hash函数最优为3个.(能够容忍最多的hash函数个数)
 * 使用的三个hash函数为
 * BKDR, SDBM, JSHash
 *
 * 注意, 在存储的数据量到2^30条时候, 误判率会急剧增加, 因此需要定时判断过滤器中的位为1的的数量是否超过50%, 超过则需要清空.
 */
class FilteRepeatedComments extends BloomFilterRedis
{
	/**
	 * 表示判断重复内容的过滤器
	 * @var string
	 */
	protected $bucket = 'rptc';

	protected $hashFunction = array('BKDRHash', 'SDBMHash', 'JSHash');
}
```

#### 结合Redis使用2

```php
<?php

use \Redis;

/**
 * 布隆过滤器
 * 
 * Class BloomFilter
 * @package Applications\Logic\Common\Redis
 */
class BloomFilter
{
    /**
     * 字节数组大小(这里因为使用的redis，支持512M的字节)
     * @var int
     */
    private $m;

    /**
     * hash函数数量
     * @var int
     */
    private $k;


    /**
     * @var string 名称
     */
    private $key;

    /**
     * BloomFilter constructor.
     * @param $key string 缓存key
     * @param int $n 加入集合的元素数量
     * @param float $falsePositiveProbability 可接受的错误率
     */
    public function __construct(string $key, int $n = 1000000, float $falsePositiveProbability = 0.0001)
    {
        $this->key = $key;
        $this->m = $this->calcBitSize($n, $falsePositiveProbability);
        $this->k = $this->getHashCount($this->m, $n);
    }

    /**
     * 根据字节数组与数据量计算hash函数的数量
     * @param $m int bit数组的宽度
     * @param $n int 加入其中的key的数量
     * @return float
     */
    private function getHashCount($m, $n) : float
    {
        return ceil(($m / $n) * log(2));
    }

    /**
     * 根据集合数与可接收的错误率去计算bit位的大小
     * m = ceil((n * log(p)) / log(1.0 / (pow(2.0, log(2.0)))));
     * m - Number of bits in the filter
     * n - Number of items in the filter
     * p - Probability of false positives, float between 0 and 1 or a number indicating 1-in-p
     *
     * @param int $setSize
     * @param float $falsePositiveProbability
     * @return int
     */
    private function calcBitSize($setSize, $falsePositiveProbability) : int
    {
        return (int) round((($setSize * log($falsePositiveProbability)) / (log(2)** 2)) * -1);
    }


    /**
     * @return string
     */
    private function getCacheKey() : string
    {
        return $this->key;
    }

    /**
     * @param $str
     * @return array
     */
    private function hashCode($str) : array
    {
        $res = array(); #put k hashing bit into $res
        $seed = crc32($str);
        mt_srand($seed); // set random seed, or mt_rand wouldn't provide same random arrays at different generation
        for($i=0 ; $i<$this->k ; $i++){
            $res[] = mt_rand(0,$this->m-1);
        }
        return $res;
    }

    /**
     * 添加元素
     * @param $filed
     */
    public function add($filed) : void
    {
        $code = $this->hashCode($filed);
        $redis = new Redis();

        $redis->multi(\Redis::PIPELINE);
        foreach($code as $codeBit){
            $redis->setBit($this->getCacheKey(), $codeBit, 1);
        }

        $redis->exec();
    }

    /**
     * 判断是否存在字段
     * @param $filed
     * @return bool
     */
    public function has($filed) : bool
    {
        $code = $this->hashCode($filed);

        $redis = new Redis();
        $redis->multi(\Redis::PIPELINE);

        foreach($code as $codeBit){
            $redis->getBit($this->getCacheKey(), $codeBit);
        }

        $result = $redis->exec();
        return !in_array(0, $result, false);
    }
}
```



## 大数据量处理

#### BitMap

```php
<?php  
// 5百万 uid 白名单 之 PHP Bitmap 处理 
class Bitmap   
{  
    private $handler = NULL;  
    private $max = 0;  
    public function __construct($file)   
    {  
        clearstatcache(true, $file);    // 是否清除真实路径缓存     
        // clearstatcache 清除文件状态缓存 (本函数缓存特定文件名的信息，因此只在对同一个文件名进行多次操作并且需要该文件信息不被缓存时才需要调用 clearstatcache()) 
        if(file_exists($file))  
            $this->handler = @fopen($file , 'r+') OR die('open bitmap file failed');  
        else  
            $this->handler = @fopen($file , 'w+') OR die('open bitmap file failed');  
  
        $this->max = file_exists($file) ? (filesize($file) * 8 - 1) : 0;  
    }  
    public function __destruct()   
    {  
        @fclose($this->handler);  
    }  
      
    private function binary_dump($binary_data)  
    {  
        return sprintf('%08d',decbin(hexdec(bin2hex($binary_data))));  
    }  
      
    private function num_check($num)  
    {  
        ($num > -1) OR die('number must be greater than -1');  
        ($num < 4294967296) or die('number must be less than 4294967296'); // 2^32  
        if ($this->max < $num) {  
            fseek($this->handler, 0, SEEK_END);  
            fwrite($this->handler , str_repeat("\x00",ceil(($num - $this->max)/8))); // fill with 0  
            $this->max = ceil($num/8)*8 - 1;  
        }         
    }  
      
    public function set($num)  
    {  
        $this->num_check($num);  
        fseek($this->handler, floor($num/8), SEEK_SET);  
        $bin = fread($this->handler, 1) | pack('C',0x100 >> fmod($num,8)+1); // mark with 1  
          
        fseek($this->handler, ftell($this->handler)-1, SEEK_SET); // write a new byte  
        fwrite($this->handler, $bin);   
        fflush($this->handler);  
    }  
      
    public function del($num)  
    {  
        $this->num_check($num);  
        fseek($this->handler, floor($num/8), SEEK_SET);  
        $bin = fread($this->handler, 1) & ~pack('C',0x100 >> fmod($num,8)+1); // mark with 0  
          
        fseek($this->handler, ftell($this->handler)-1, SEEK_SET); // write a new byte  
        fwrite($this->handler, $bin);   
        fflush($this->handler);  
    }     
      
    public function find($num)  
    {  
        if (fseek($this->handler, floor($num/8), SEEK_SET) == -1) return FALSE;  
        $bin = fread($this->handler , 1);  
        if ($bin === FALSE || strlen($bin) == 0) return FALSE;  
  
        $bin = $bin & pack('C',0x100 >> fmod($num,8)+1);  
        if($bin === "\x00") return FALSE;  
        return TRUE;  
    }  
}  
  
$b = new Bitmap('cache.dat');  
  
// 设置白名单  
$b->set(1); 
$b->set(3); 
$b->set(5);  
$b->set(7); 
$b->set(9); 
$b->set(501);  
  
$uid = 501;  
var_dump($b->find($uid)); // 查找白名单  
  
$b->del($uid); // 删除白名单  
var_dump($b->find($uid)); // 查找白名单  
```

#### HashMap

```php
class HashMap
{
	private $H_table;

	public function __construct()
	{
		$this->H_table = [];
	}

	// 向HashMap添加键值对
	public function put($key,$value)
	{
		if( !array_key_exists($key,$this->H_table) ){
			$this->H_table[$key] = $value;
			return null;
		}else{
			$tempValue = $this->H_table[$key];
			$this->H_table[$key] = $value;
			return $tempValue;
		}
	}

	// 根据key获取值
	public function get($key)
	{
		return array_key_exists($key,$this->H_table) ? $this->H_table[$key] : null;
	}

	// 移除HashMap所有键值对
	public function remove($key)
	{
		$temp_table = [];
		if( array_key_exists($key,$this->H_table) ){
			$tempValue = $this->H_table[$key];
			while ($curValue = current($this->H_table) ) {
				if( key($this->H_table) !== $key ){
					$temp_table[key($this->H_table)] = $curValue;
				}
				next($this->H_table);
			}

			$this->H_table = null;
			$this->H_table = $temp_table;
			return $tempValue;
		}

		return null;
	}

	// 获取HashMap所有键名
	public function keys()
	{
		return array_keys($this->H_table);
	}

	// 获取HashMap所有键值
	public function values()
	{
		return array_values($this->H_table);
	}

	// 将一个HashMap中键值对放置到当前HashMap中
	public function putAll($map)
	{
		if( !$map->isEmpty() && $map->size() > 0 ){
			$keys = $map->keys();
			foreach ($keys as $key) {
				$this->put($key,$map->get($key));
			}
		}
	}

	// 移除HashMap所有元素
	public function removeAll()
	{
		$this->H_table = null;
		$this->H_table = [];
	}

	// HashMap是否包含指定值
	public function containsValue($value)
	{
		while ( $curValue = current($this->H_table) ) {
			if($curValue == $value){
				return true;
			}
			next($this->H_table);
		}
		return false;
	}

	// HashMap是否包含指定键
	public function containsKey($key)
	{
		return array_key_exists($key,$this->H_table);
	}

	// 获取HashMap中元素个数
	public function size()
	{
		return count($this->H_table);
	}

	// 判断HashMap是否为空
	public function isEmpty()
	{
		return count($this->H_table) === 0;
	}

	// 打印HashMap数据
	public function toString()
	{
		print_r($this->H_table);
	}
}
```



