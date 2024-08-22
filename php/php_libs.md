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

#### 多文件上传

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

#### 支持多种上传方式

```php
<?php

class Uploader
{
    private $fileField; //文件域名
    private $file; //文件上传对象
    private $base64; //文件上传对象
    private $config; //配置信息
    private $oriName; //原始文件名
    private $fileName; //新文件名
    private $fullName; //完整文件名,即从当前配置目录开始的URL
    private $filePath; //完整文件名,即从当前配置目录开始的URL
    private $fileSize; //文件大小
    private $fileType; //文件类型
    private $stateInfo; //上传状态信息,
    private $stateMap = array( //上传状态映射表，国际化用户需考虑此处数据的国际化
        "SUCCESS", //上传成功标记，在UEditor中内不可改变，否则flash判断会出错
        "文件大小超出 upload_max_filesize 限制",
        "文件大小超出 MAX_FILE_SIZE 限制",
        "文件未被完整上传",
        "没有文件被上传",
        "上传文件为空",
        "ERROR_TMP_FILE" => "临时文件错误",
        "ERROR_TMP_FILE_NOT_FOUND" => "找不到临时文件",
        "ERROR_SIZE_EXCEED" => "文件大小超出网站限制",
        "ERROR_TYPE_NOT_ALLOWED" => "文件类型不允许",
        "ERROR_CREATE_DIR" => "目录创建失败",
        "ERROR_DIR_NOT_WRITEABLE" => "目录没有写权限",
        "ERROR_FILE_MOVE" => "文件保存时出错",
        "ERROR_FILE_NOT_FOUND" => "找不到上传文件",
        "ERROR_WRITE_CONTENT" => "写入文件内容错误",
        "ERROR_UNKNOWN" => "未知错误",
        "ERROR_DEAD_LINK" => "链接不可用",
        "ERROR_HTTP_LINK" => "链接不是http链接",
        "ERROR_HTTP_CONTENTTYPE" => "链接contentType不正确"
    );
    /**
     * 构造函数
     * @param string $fileField 表单名称
     * @param array $config 配置项
	 * @param string $type	处理文件上传的方式
     */
    public function __construct($fileField, $config, $type = "upload")
    {
        $this->fileField = $fileField;
        $this->config = $config;
        $this->type = $type;
        if ($type == "remote") {
            $this->saveRemote();
        } else if($type == "base64") {
            $this->upBase64();
        } else {
            $this->upFile();
        }
        $this->stateMap['ERROR_TYPE_NOT_ALLOWED'] = mb_convert_encoding($this->stateMap['ERROR_TYPE_NOT_ALLOWED'], 'utf-8', 'auto');
    }
    /**
     * 上传文件的主处理方法
     * @return mixed
     */
    private function upFile()
    {
        $file = $this->file = $_FILES[$this->fileField];
        if (!$file) {
            $this->stateInfo = $this->getStateInfo("ERROR_FILE_NOT_FOUND");
            return;
        }
        if ($this->file['error']) {
            $this->stateInfo = $this->getStateInfo($file['error']);
            return;
        } else if (!file_exists($file['tmp_name'])) {
            $this->stateInfo = $this->getStateInfo("ERROR_TMP_FILE_NOT_FOUND");
            return;
        } else if (!is_uploaded_file($file['tmp_name'])) {
            $this->stateInfo = $this->getStateInfo("ERROR_TMPFILE");
            return;
        }
        $this->oriName = $file['name'];
        $this->fileSize = $file['size'];
        $this->fileType = $this->getFileExt();
        $this->fullName = $this->getFullName();
        $this->filePath = $this->getFilePath();
        $this->fileName = $this->getFileName();
        $dirname = dirname($this->filePath);
        //检查文件大小是否超出限制
        if (!$this->checkSize()) {
            $this->stateInfo = $this->getStateInfo("ERROR_SIZE_EXCEED");
            return;
        }
        //检查是否不允许的文件格式
        if (!$this->checkType()) {
            $this->stateInfo = $this->getStateInfo("ERROR_TYPE_NOT_ALLOWED");
            return;
        }
        //创建目录失败
        if (!file_exists($dirname) && !mkdir($dirname, 0777, true)) {
            $this->stateInfo = $this->getStateInfo("ERROR_CREATE_DIR");
            return;
        } else if (!is_writeable($dirname)) {
            $this->stateInfo = $this->getStateInfo("ERROR_DIR_NOT_WRITEABLE");
            return;
        }
        //移动文件
        if (!(move_uploaded_file($file["tmp_name"], $this->filePath) && file_exists($this->filePath))) { //移动失败
            $this->stateInfo = $this->getStateInfo("ERROR_FILE_MOVE");
        } else { //移动成功
            $this->stateInfo = $this->stateMap[0];
        }
    }
    /**
     * 处理base64编码的图片上传
     * @return mixed
     */
    private function upBase64()
    {
        $base64Data = $_POST[$this->fileField];
        $img = base64_decode($base64Data);
        $this->oriName = $this->config['oriName'];
        $this->fileSize = strlen($img);
        $this->fileType = $this->getFileExt();
        $this->fullName = $this->getFullName();
        $this->filePath = $this->getFilePath();
        $this->fileName = $this->getFileName();
        $dirname = dirname($this->filePath);
        //检查文件大小是否超出限制
        if (!$this->checkSize()) {
            $this->stateInfo = $this->getStateInfo("ERROR_SIZE_EXCEED");
            return;
        }
        //创建目录失败
        if (!file_exists($dirname) && !mkdir($dirname, 0777, true)) {
            $this->stateInfo = $this->getStateInfo("ERROR_CREATE_DIR");
            return;
        } else if (!is_writeable($dirname)) {
            $this->stateInfo = $this->getStateInfo("ERROR_DIR_NOT_WRITEABLE");
            return;
        }
        //移动文件
        if (!(file_put_contents($this->filePath, $img) && file_exists($this->filePath))) { //移动失败
            $this->stateInfo = $this->getStateInfo("ERROR_WRITE_CONTENT");
        } else { //移动成功
            $this->stateInfo = $this->stateMap[0];
        }
    }
    /**
     * 拉取远程图片
     * @return mixed
     */
    private function saveRemote()
    {
        $imgUrl = htmlspecialchars($this->fileField);
        $imgUrl = str_replace("&amp;", "&", $imgUrl);
	    
        //获取带有GET参数的真实图片url路径
        $pathRes     = parse_url($imgUrl);
        $queryString = isset($pathRes['query']) ? $pathRes['query'] : '';
        $imgUrl      = str_replace('?' . $queryString, '', $imgUrl);
        //http开头验证
        if (strpos($imgUrl, "http") !== 0) {
            $this->stateInfo = $this->getStateInfo("ERROR_HTTP_LINK");
            return;
        }
        //获取请求头并检测死链
        $heads = get_headers($imgUrl, 1); 
        if (!(stristr($heads[0], "200") && stristr($heads[0], "OK"))) {
            $this->stateInfo = $this->getStateInfo("ERROR_DEAD_LINK");
            return;
        }
        //格式验证(扩展名验证和Content-Type验证)
        $fileType = strtolower(strrchr($imgUrl, '.'));
        if (!in_array($fileType, $this->config['allowFiles']) || !isset($heads['Content-Type']) || !stristr($heads['Content-Type'], "image")) {
            $this->stateInfo = $this->getStateInfo("ERROR_HTTP_CONTENTTYPE");
            return;
        }
        //打开输出缓冲区并获取远程图片
        ob_start();
        $context = stream_context_create(
            array('http' => array(
                'follow_location' => false // don't follow redirects
            ))
        );
        readfile($imgUrl . '?' . $queryString, false, $context); //读取文件并写入到输出缓冲
        $img = ob_get_contents();
        ob_end_clean();
        preg_match("/[\/]([^\/]*)[\.]?[^\.\/]*$/", $imgUrl, $m);
        $this->oriName = $m ? $m[1]:"";
        $this->fileSize = strlen($img);
        $this->fileType = $this->getFileExt();
        $this->fullName = $this->getFullName();
        $this->filePath = $this->getFilePath();
        $this->fileName = $this->getFileName();
        $dirname = dirname($this->filePath);
        //检查文件大小是否超出限制
        if (!$this->checkSize()) {
            $this->stateInfo = $this->getStateInfo("ERROR_SIZE_EXCEED");
            return;
        }
        //检查文件内容是否真的是图片
        if (substr(mime_content_type($this->filePath), 0, 5) != 'image') {
            $this->stateInfo = $this->getStateInfo("ERROR_TYPE_NOT_ALLOWED");
            return;
        }
        //创建目录失败
        if (!file_exists($dirname) && !mkdir($dirname, 0777, true)) {
            $this->stateInfo = $this->getStateInfo("ERROR_CREATE_DIR");
            return;
        } else if (!is_writeable($dirname)) {
            $this->stateInfo = $this->getStateInfo("ERROR_DIR_NOT_WRITEABLE");
            return;
        }
        //移动文件
        if (!(file_put_contents($this->filePath, $img) && file_exists($this->filePath))) { //移动失败
            $this->stateInfo = $this->getStateInfo("ERROR_WRITE_CONTENT");
        } else { //移动成功
            $this->stateInfo = $this->stateMap[0];
        }
    }
    /**
     * 上传错误检查
     * @param $errCode
     * @return string
     */
    private function getStateInfo($errCode)
    {
        return !$this->stateMap[$errCode] ? $this->stateMap["ERROR_UNKNOWN"] : $this->stateMap[$errCode];
    }
    /**
     * 获取文件扩展名
     * @return string
     */
    private function getFileExt()
    {
        return strtolower(strrchr($this->oriName, '.'));
    }
    /**
     * 重命名文件
     * @return string
     */
    private function getFullName()
    {
        //替换日期事件
        $t = time();
        $d = explode('-', date("Y-y-m-d-H-i-s"));
        $format = $this->config["pathFormat"];
        $format = str_replace("{yyyy}", $d[0], $format);
        $format = str_replace("{yy}", $d[1], $format);
        $format = str_replace("{mm}", $d[2], $format);
        $format = str_replace("{dd}", $d[3], $format);
        $format = str_replace("{hh}", $d[4], $format);
        $format = str_replace("{ii}", $d[5], $format);
        $format = str_replace("{ss}", $d[6], $format);
        $format = str_replace("{time}", $t, $format);
        //过滤文件名的非法字符,并替换文件名
        $oriName = substr($this->oriName, 0, strrpos($this->oriName, '.'));
        $oriName = preg_replace("/[\|\?\"\<\>\/\*\\\\]+/", '', $oriName);
        $format = str_replace("{filename}", $oriName, $format);
        //替换随机字符串
        $randNum = rand(1, 10000000000) . rand(1, 10000000000);
        if (preg_match("/\{rand\:([\d]*)\}/i", $format, $matches)) {
            $format = preg_replace("/\{rand\:[\d]*\}/i", substr($randNum, 0, $matches[1]), $format);
        }
        if($this->fileType){
            $ext = $this->fileType;
        } else {
            $ext = $this->getFileExt();
        }
        return $format . $ext;
    }
    /**
     * 获取文件名
     * @return string
     */
    private function getFileName () {
        return substr($this->filePath, strrpos($this->filePath, '/') + 1);
    }
    /**
     * 获取文件完整路径
     * @return string
     */
    private function getFilePath()
    {
        $fullname = $this->fullName;
        $rootPath = $_SERVER['DOCUMENT_ROOT'];
        if (substr($fullname, 0, 1) != '/') {
            $fullname = '/' . $fullname;
        }
        return $rootPath . $fullname;
    }
    /**
     * 文件类型检测
     * @return bool
     */
    private function checkType()
    {
        return in_array($this->getFileExt(), $this->config["allowFiles"]);
    }
    /**
     * 文件大小检测
     * @return bool
     */
    private function  checkSize()
    {
        return $this->fileSize <= ($this->config["maxSize"]);
    }
    /**
     * 获取当前上传成功文件的各项信息
     * @return array
     */
    public function getFileInfo()
    {
        return array(
            "state" => $this->stateInfo,
            "url" => $this->fullName,
            "title" => $this->fileName,
            "original" => $this->oriName,
            "type" => $this->fileType,
            "size" => $this->fileSize
        );
    }
}
```









## 数据库

#### PDO操作

```php
class crud
{

    private $db;

    /**
     *
     * Set variables
     *
     */
    public function __set($name, $value)
    {
        switch($name)
        {
            case 'username':
            $this->username = $value;
            break;

            case 'password':
            $this->password = $value;
            break;

            case 'dsn':
            $this->dsn = $value;
            break;

            default:
            throw new Exception("$name is invalid");
        }
    }

    /**
     *
     * @check variables have default value
     *
     */
    public function __isset($name)
    {
        switch($name)
        {
            case 'username':
            $this->username = null;
            break;

            case 'password':
            $this->password = null;
            break;
        }
    }

        /**
         *
         * @Connect to the database and set the error mode to Exception
         *
         * @Throws PDOException on failure
         *
         */
        public function conn()
        {
            isset($this->username);
            isset($this->password);
            if (!$this->db instanceof PDO)
            {
                $this->db = new PDO($this->dsn, $this->username, $this->password);
                $this->db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            }
        }


        /***
         *
         * @select values from table
         *
         * @access public
         *
         * @param string $table The name of the table
         *
         * @param string $fieldname
         *
         * @param string $id
         *
         * @return array on success or throw PDOException on failure
         *
         */
        public function dbSelect($table, $fieldname=null, $id=null)
        {
            $this->conn();
            $sql = "SELECT * FROM `$table` WHERE `$fieldname`=:id";
            $stmt = $this->db->prepare($sql);
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        }


        /**
         *
         * @execute a raw query
         *
         * @access public
         *
         * @param string $sql
         *
         * @return array
         *
         */
        public function rawSelect($sql)
        {
            $this->conn();
            return $this->db->query($sql);
        }

        /**
         *
         * @run a raw query
         *
         * @param string The query to run
         *
         */
        public function rawQuery($sql)
        {
            $this->conn();
            $this->db->query($sql);
        }


        /**
         *
         * @Insert a value into a table
         *
         * @acces public
         *
         * @param string $table
         *
         * @param array $values
         *
         * @return int The last Insert Id on success or throw PDOexeption on failure
         *
         */
        public function dbInsert($table, $values)
        {
            $this->conn();
            /*** snarg the field names from the first array member ***/
            $fieldnames = array_keys($values[0]);
            /*** now build the query ***/
            $size = sizeof($fieldnames);
            $i = 1;
            $sql = "INSERT INTO $table";
            /*** set the field names ***/
            $fields = '( ' . implode(' ,', $fieldnames) . ' )';
            /*** set the placeholders ***/
            $bound = '(:' . implode(', :', $fieldnames) . ' )';
            /*** put the query together ***/
            $sql .= $fields.' VALUES '.$bound;

            /*** prepare and execute ***/
            $stmt = $this->db->prepare($sql);
            foreach($values as $vals)
            {
                $stmt->execute($vals);
            }
        }

        /**
         *
         * @Update a value in a table
         *
         * @access public
         *
         * @param string $table
         *
         * @param string $fieldname, The field to be updated
         *
         * @param string $value The new value
         *
         * @param string $pk The primary key
         *
         * @param string $id The id
         *
         * @throws PDOException on failure
         *
         */
        public function dbUpdate($table, $fieldname, $value, $pk, $id)
        {
            $this->conn();
            $sql = "UPDATE `$table` SET `$fieldname`='{$value}' WHERE `$pk` = :id";
            $stmt = $this->db->prepare($sql);
            $stmt->bindParam(':id', $id, PDO::PARAM_STR);
            $stmt->execute();
        }


        /**
         *
         * @Delete a record from a table
         *
         * @access public
         *
         * @param string $table
         *
         * @param string $fieldname
         *
         * @param string $id
         *
         * @throws PDOexception on failure
         *
         */
        public function dbDelete($table, $fieldname, $id)
        {
            $this->conn();
            $sql = "DELETE FROM `$table` WHERE `$fieldname` = :id";
            $stmt = $this->db->prepare($sql);
            $stmt->bindParam(':id', $id, PDO::PARAM_STR);
            $stmt->execute();
        }
    } /*** end of class ***/
```





## 日志

#### 日志类

```php
<?php
/**
 * php日志类
 *
 * Description: 
 * 1.自定义日志根目录及日志文件名称。
 * 2.使用日期时间格式自定义日志目录。
 * 3.自动创建不存在的日志目录。
 * 4.记录不同分类的日志，例如信息日志，警告日志，错误日志。
 * 5.可自定义日志配置，日志根据标签调用不同的日志配置。
 *
 * Func
 * public  static set_config 设置配置
 * public  static get_logger 获取日志类对象
 * public  info              写入信息日志
 * public  warn              写入警告日志
 * public  error             写入错误日志
 * private add               写入日志
 * private create_log_path   创建日志目录
 * private get_log_file      获取日志文件名称
 */
class LOG {

    // 日志根目录
    private $_log_path = '.';

    // 日志文件
    private $_log_file = 'default.log';

    // 日志自定义目录
    private $_format = 'Y/m/d';

    // 日志标签
    private $_tag = 'default';

    // 总配置设定
    private static $_CONFIG;

    /**
     * 设置配置
     * @param  Array $config 总配置设定
     */
    public static function set_config($config=array()){
        self::$_CONFIG = $config; 
    }

    /**
     * 获取日志类对象
     * @param  Array $config 总配置设定
     * @return Obj
     */
    public static function get_logger($tag='default'){

        // 根据tag从总配置中获取对应设定，如不存在使用default设定
        $config = isset(self::$_CONFIG[$tag])? self::$_CONFIG[$tag] : (isset(self::$_CONFIG['default'])? self::$_CONFIG['default'] : array());

        // 设置标签
        $config['tag'] = $tag!='' && $tag!='default'? $tag : '-';

        // 返回日志类对象
        return new LOG($config);

    }

    /**
     * 初始化
     * @param Array $config 配置设定
     */
    public function __construct($config=array()){

        // 日志根目录
        if(isset($config['log_path'])){
            $this->_log_path = $config['log_path'];
        }

        // 日志文件
        if(isset($config['log_file'])){
            $this->_log_file = $config['log_file'];
        }

        // 日志自定义目录
        if(isset($config['format'])){
            $this->_format = $config['format'];
        }

        // 日志标签
        if(isset($config['tag'])){
            $this->_tag = $config['tag'];
        }

    }

    /**
     * 写入信息日志
     * @param  String $data 信息数据
     * @return Boolean
     */
    public function info($data){
        return $this->add('INFO', $data);
    }

    /**
     * 写入警告日志
     * @param  String  $data 警告数据
     * @return Boolean
     */
    public function warn($data){
        return $this->add('WARN', $data);
    }

    /**
     * 写入错误日志
     * @param  String  $data 错误数据
     * @return Boolean
     */
    public function error($data){
        return $this->add('ERROR', $data);
    }

    /**
     * 写入日志
     * @param  String  $type 日志类型
     * @param  String  $data 日志数据
     * @return Boolean
     */
    private function add($type, $data){

        // 获取日志文件
        $log_file = $this->get_log_file();

        // 创建日志目录
        $is_create = $this->create_log_path(dirname($log_file));

        // 创建日期时间对象
        $dt = new DateTime;

        // 日志内容
        $log_data = sprintf('[%s] %-5s %s %s'.PHP_EOL, $dt->format('Y-m-d H:i:s'), $type, $this->_tag, $data);

        // 写入日志文件
        if($is_create){
            return file_put_contents($log_file, $log_data, FILE_APPEND);
        }

        return false;

    }

    /**
     * 创建日志目录
     * @param  String  $log_path 日志目录
     * @return Boolean
     */
    private function create_log_path($log_path){
        if(!is_dir($log_path)){
            return mkdir($log_path, 0777, true);
        }
        return true;
    }

    /**
     * 获取日志文件名称
     * @return String
     */
    private function get_log_file(){

        // 创建日期时间对象
        $dt = new DateTime;

        // 计算日志目录格式
        return sprintf("%s/%s/%s", $this->_log_path, $dt->format($this->_format), $this->_log_file);
    
    }

}
```







## 服务

#### RPC服务

```php
// 1.服务端
<?php  

class RpcServer 
{

    protected $serv = null;
 
    public function __construct($host, $port, $path) {
        //创建一个tcp socket服务
        $this->serv = stream_socket_server("tcp://{$host}:{$port}", $errno, $errstr); 
        if (!$this->serv) {
            exit("{$errno} : {$errstr} \n");
        }
        //判断我们的RPC服务目录是否存在
        $realPath = realpath(__DIR__ . $path);
        if ($realPath === false || !file_exists($realPath)) {
            exit("{$path} error \n");
        }
 
        while (true) {
            $client = stream_socket_accept($this->serv);
 
            if ($client) {
                //这里为了简单，我们一次性读取
                $buf = fread($client, 2048);
                //解析客户端发送过来的协议
                $classRet = preg_match('/Rpc-Class:\s(.*);\r\n/i', $buf, $class);
                $methodRet = preg_match('/Rpc-Method:\s(.*);\r\n/i', $buf, $method);
                $paramsRet = preg_match('/Rpc-Params:\s(.*);\r\n/i', $buf, $params);
                 
                if($classRet && $methodRet) {
                    $class = ucfirst($class[1]);
                    $file = $realPath . '/' . $class . '.php';
                    //判断文件是否存在，如果有，则引入文件
                    if(file_exists($file)) {
                        require_once $file;
                        //实例化类，并调用客户端指定的方法
                        $obj = new $class();
                        //如果有参数，则传入指定参数
                        if(!$paramsRet) {
                            $data = $obj->$method[1]();
                        } else {
                            $data = $obj->$method[1](json_decode($params[1], true));
                        }
                        //把运行后的结果返回给客户端
                        fwrite($client, $data);
                    }
                } else {
                    fwrite($client, 'class or method error');
                }
                //关闭客户端
                fclose($client);
            }
        }
    }
 
    public function __destruct() {
        fclose($this->serv);
    }
}
 
new RpcServer('127.0.0.1', 8888, './service');


// 2.客户端
<?php 

class RpcClient {
    protected $urlInfo = array();
     
    public function __construct($url) {
        //解析URL
        $this->urlInfo = parse_url($url);
        if(!$this->urlInfo) {
            exit("{$url} error \n");
        }
    }
     
    public function __call($method, $params) {
        //创建一个客户端
        $client = stream_socket_client("tcp://{$this->urlInfo['host']}:{$this->urlInfo['port']}", $errno, $errstr);
        if (!$client) {
            exit("{$errno} : {$errstr} \n");
        }
        //传递调用的类名
        $class = basename($this->urlInfo['path']);
        $proto = "Rpc-Class: {$class};" . PHP_EOL;
        //传递调用的方法名
        $proto .= "Rpc-Method: {$method};" . PHP_EOL;
        //传递方法的参数
        $params = json_encode($params);
        $proto .= "Rpc-Params: {$params};" . PHP_EOL;
        //向服务端发送我们自定义的协议数据
        fwrite($client, $proto);
        //读取服务端传来的数据
        $data = fread($client, 2048);
        //关闭客户端
        fclose($client);
        return $data;
    }
}
 
$cli = new RpcClient('http://127.0.0.1:8888/test');
echo $cli->hehe();
echo $cli->hehe2(array('name' => 'test', 'age' => 27));


// 3.测试数据
<?php  

class Test {
    public function hehe() {
        return 'hehe';
    }
    public function hehe2($params) {
        return json_encode($params);
    }
}


//项目结构
RPC
| - - service
| - - - Test.php
| - - RpcClient.php
| - - RpcServer.php


```

#### 协程处理

```php
// 协程实例

class Task {
    protected $taskId;//任务id
    protected $coroutine;//生成器
    protected $sendValue = null;//生成器send值
    protected $beforeFirstYield = true;//迭代指针是否是第一个
 
    public function __construct($taskId, Generator $coroutine) {
        $this->taskId = $taskId;
        $this->coroutine = $coroutine;
    }
 
    public function getTaskId() {
        return $this->taskId;
    }
 
    /**
     * 设置插入数据
     * @param $sendValue
     */
    public function setSendValue($sendValue) {
        $this->sendValue = $sendValue;
    }
 
    /**
     * send数据进行迭代
     * @return mixed
     */
    public function run() {
        //如果是
        if ($this->beforeFirstYield) {
            $this->beforeFirstYield = false;
            var_dump($this->coroutine->current());
            return $this->coroutine->current();
        } else {
            $retval = $this->coroutine->send($this->sendValue);
            $this->sendValue = null;
            return $retval;
        }
    }
 
    /**
     * 是否完成
     * @return bool
     */
    public function isFinished() {
        return !$this->coroutine->valid();
    }
}


/**
 * 任务调度
 * Class Scheduler
 */
class Scheduler {
    protected $maxTaskId = 0;//任务id
    protected $taskMap = []; // taskId => task
    protected $taskQueue;//任务队列
 
    public function __construct() {
        $this->taskQueue = new SplQueue();
    }
 
    public function newTask(Generator $coroutine) {
        $tid = ++$this->maxTaskId;
        //新增任务
        $task = new Task($tid, $coroutine);
        $this->taskMap[$tid] = $task;
        $this->schedule($task);
        return $tid;
    }
 
    /**
     * 任务入列
     * @param Task $task
     */
    public function schedule(Task $task) {
        $this->taskQueue->enqueue($task);
    }
 
    public function run() {
        while (!$this->taskQueue->isEmpty()) {
            //任务出列进行遍历生成器数据
            $task = $this->taskQueue->dequeue();
            $task->run();
 
            if ($task->isFinished()) {
                //完成则删除该任务
                unset($this->taskMap[$task->getTaskId()]);
            } else {
                //继续入列
                $this->schedule($task);
            }
        }
    }
}

function task1()
{
    for ($i = 0; $i <= 300; $i++) {
        //写入文件,大概要3000微秒
        usleep(3000);
        echo "写入文件{$i}\n";
        yield $i;
    }
}
 
function task2()
{
    for ($i = 0; $i <= 500; $i++) {
        //发送邮件给500名会员,大概3000微秒
        usleep(3000);
        echo "发送邮件{$i}\n";
        yield $i;
    }
}
 
function task3()
{
    for ($i = 0; $i <= 100; $i++) {
        //模拟插入100条数据,大概3000微秒
        usleep(3000);
        echo "插入数据{$i}\n";
        yield $i;
    }
}
 
$scheduler = new Scheduler;
$scheduler->newTask(task1());
$scheduler->newTask(task2());
$scheduler->newTask(task3());
 
$scheduler->run();
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



## 数据处理

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



#### 数据操作-带锁(文件,数据库,memcache)

```php
<?php 

class LockSystem
{
 const LOCK_TYPE_DB = 'SQLLock';
 const LOCK_TYPE_FILE = 'FileLock';
 const LOCK_TYPE_MEMCACHE = 'MemcacheLock';

 private $_lock = null;
 private static $_supportLocks = array('FileLock', 'SQLLock', 'MemcacheLock'); 

 public function __construct($type, $options = array()) 
 {
  if(false == empty($type))
  {
   $this->createLock($type, $options);
  }
 } 

 public function createLock($type, $options=array())
 {
  if (false == in_array($type, self::$_supportLocks))
  {
   throw new Exception("not support lock of ${type}");
  }
  $this->_lock = new $type($options);
 }  
 public function getLock($key, $timeout = ILock::EXPIRE)
 {
  if (false == $this->_lock instanceof ILock) 
  {
   throw new Exception('false == $this->_lock instanceof ILock');   
  } 
  $this->_lock->getLock($key, $timeout); 
 }

 public function releaseLock($key)
 {
  if (false == $this->_lock instanceof ILock) 
  {
   throw new Exception('false == $this->_lock instanceof ILock');   
  } 
  $this->_lock->releaseLock($key);   
 } 
}
interface ILock
{
 const EXPIRE = 5;
 public function getLock($key, $timeout=self::EXPIRE);
 public function releaseLock($key);
}

class FileLock implements ILock
{

 private $_fp;
 private $_single;

 public function __construct($options)
 {
  if (isset($options['path']) && is_dir($options['path']))
  {
    $this->_lockPath = $options['path'].'/';
  }
  else
  {
    $this->_lockPath = '/tmp/'; //将文件锁放置在临时目录中
  }

  $this->_single = isset($options['single'])?$options['single']:false;
 }
 public function getLock($key, $timeout=self::EXPIRE)
 {
    $startTime = Timer::getTimeStamp();

    $file = md5(__FILE__.$key); //文件名称要唯一 (一个功能对应一个文件锁)
    $this->fp = fopen($this->_lockPath.$file.'.lock', "w+");
    if (true || $this->_single)
    {
      $op = LOCK_EX + LOCK_NB; //在锁定的时候,不希望被阻塞时添加  LOCK_NB
    }
    else
    {
      $op = LOCK_EX; //独占 (写入)
    }

    if (false == flock($this->fp, $op, $a))
    {
      throw new Exception('failed');
    }

    return true;
 }
 public function releaseLock($key)
 {
    flock($this->fp, LOCK_UN); //解除锁定
    fclose($this->fp); //释放文件
 }
}

class SQLLock implements ILock
{

 public function __construct($options)
 {
    $this->_db = new mysql(); 
 }

 public function getLock($key, $timeout=self::EXPIRE)
 {  
    $sql = "SELECT GET_LOCK('".$key."', '".$timeout."')";
    $res = $this->_db->query($sql);
    return $res;
 }

 public function releaseLock($key)
 {
    $sql = "SELECT RELEASE_LOCK('".$key."')";
    return $this->_db->query($sql);
 }
}

class MemcacheLock implements ILock
{

 public function __construct($options)
 {

    $this->memcache = new Memcache();
 }

 public function getLock($key, $timeout=self::EXPIRE)
 {  
    $waitime = 20000;
    $totalWaitime = 0;
    $time = $timeout*1000000; //5秒钟尝试时间
    while ($totalWaitime < $time && false == $this->memcache->add($key, 1, $timeout)) 
    {
      usleep($waitime);
      $totalWaitime += $waitime;
    }
    if ($totalWaitime >= $time)
      throw new Exception('can not get lock for waiting '.$timeout.'s.');

 }

 public function releaseLock($key)
 {
    $this->memcache->delete($key);
 }
}

// 调用方式

//  try
//  {
//   //创建锁(推荐使用MemcacheLock)
//   $lockSystem = new LockSystem(LockSystem::LOCK_TYPE_MEMCACHE);    

//   //获取锁
//   $lockKey = 'pay'.$userId; //确定唯一性
//   $lockSystem->getLock($lockKey,8);

//   //取出总额
//   $total = getUserLeftMoney($userId);

//   //花费大于剩余
//   if($money > $total)
//   {
//    $ret = false; 
//   }
//   else
//   { 
//    //余额
//    $left = $total - $money;

//    //更新余额
//    $ret = setUserLeftMoney($userId,$left);
//   }

//   //释放锁
//   $lockSystem->releaseLock($lockKey); 
//  }
//  catch (Exception $e)
//  {
//   //释放锁
//   $lockSystem->releaseLock($lockKey);  
//  }

// }
```

#### 生成请求ID

```php
<?php
/**
 * PHP生成唯一RequestID类
 * Description:
 * PHP实现生成唯一RequestID类，使用session_create_id()与uniqid()方法实现，保证唯一性。
 *
 * Func:
 * public  generate 生成唯一请求id
 * private format   格式化请求id
 */
class RequestID{ 

    /**
     * 生成唯一请求id
     * @return String
     */
    public static function generate(){
        // 使用session_create_id()方法创建前缀
        $prefix = session_create_id(date('YmdHis'));

        // 使用uniqid()方法创建唯一id
        $request_id = strtoupper(md5(uniqid($prefix, true)));

        // 格式化请求id
        return self::format($request_id);

    }

    /**
     * 格式化请求id
     * @param  String $request_id 请求id
     * @param  Array  $format     格式
     * @return String
     */
    private static function format($request_id, $format='8,4,4,4,12'){

        $tmp = array();
        $offset = 0;

        $cut = explode(',', $format);

        // 根据设定格式化
        if($cut){
            foreach($cut as $v){
                $tmp[] = substr($request_id, $offset, $v);
                $offset += $v;
            }
        }

        // 加入剩余部分
        if($offset<strlen($request_id)){
            $tmp[] = substr($request_id, $offset);
        }

        return implode('-', $tmp);

    }

}
echo 
RequestID::generate();
```

#### 生成随机字符串

```php
class randomPassword{

function __construct($passType='alphanumeric', $length=8, $rangeLength=9){
  $this->setLength($length);
  $this->setRangeLength($rangeLength);
  $this->passType = $this->setPassType($passType);
}

function setRangeLength($rangeLength){
  $this->rangeLength=$rangeLength;
}

// set the length of the password
private function setLength($length){
  $this->length=$length;
}


// set the type of password
private function setPassType($passType){
  return $passType.'Chars';
}

// return an array of numbers
private function numericChars(){
  return range(0, $this->rangeLength);
}

// return an array of chars
private function alphaChars(){
  return range('a', 'z');
}

// return an array of alphanumeric chars
private function alphaNumericChars(){
  return array_merge($this->numericChars(), $this->alphaChars());
}

// return a string of chars
private function makeString(){
  // here we set the function to call based on the password type
  $funcName = $this->passType;
  return implode($this->$funcName());
}

// shuffle the chars and return $length of chars
public function makePassword(){
  return substr(str_shuffle($this->makeString()), 1, $this->length);
}

} // end class

  function randomPassword($length) {
  // create an array of chars to use as password
  $chars = implode(array_merge(range(0,9), range('a', 'z')));

  // randomly snarf $length number of array keys
  return substr(str_shuffle($chars), 1, $length);

}
  echo randomPassword(8).'<br />';

try
    {
    $obj = new randomPassword('alphanumeric', 16, 100);
    echo $obj->makePassword().'<br />';
    }
catch(Exception $ex)
    {
    echo $ex->getMessage();
    }

```



#### 频繁访问限制

```php
class FrequencyLimit
{

	const DEFAULT_EXPIRE_TIME = 3600*24*7; //默认自动过期时间

	static $r = null;
	// 初始化Redis
	public function __construct()
	{
		// 初始化Redis
		self::$r = new Client([
			'host'	=>	\Env::get(ENV.'.redis_host'),
			'port'	=>	\Env::get(ENV.'.redis_port'),
			'database'=> 5,
		]); 
	} 

	// ip限制
	public function ip(string $ip, int $time, int $number )
	{
		$key = C::IP_LIMIT . $ip;
		return $this->do($key,$time,$number);
	}

	// 接口限制
	public function api(string $appid, string $url, int $time, int $number)
	{
		$key = C::API_LIMIT . $appid.'_'.$url;
		return $this->do($key,$time,$number);
	}

	// 并发限制
	public function concurrent(string $appid,string $url,int $time,int $number)
	{
		$key = C::API_CONCURRENT_LIMIT . $appid . '_' . $url . '_' . time();
		return $this->do($key,$time,$number);
	}

	// 频次间隔限制
	public function apiInterval(string $appid, string $url, int $interval)
	{
		$key = C::API_INTERVAL_LIMIT . $appid.'_'.$url;
		return $this->run($key,$interval);
	}

	/**
	 * 执行频次限制
	 * @param  string $key    key键名
	 * @param  int    $time   时间范围[秒]
	 * @param  int    $number 操作次数
	 * @param  array  $expire 封禁时间['type'=>1,'ttl'=>'过期时间'],['type'=>2,'ttl'=>'具体过期时间戳']
	 * @return bool   结果
	 */
	private function do($key, $time, $number, $expire=[])
	{
		$current = intval(self::$r->get($key) );
		if($current >= $number) return false;

		$current = self::$r->incr($key);
		if($current === 1) self::$r->expire($key,$time);
		if($current < $number) return true;

		if($expire){
			$type = !$expire['type'] ? 0 : intval($expire['type']);
			$ttl = !$expire['ttl'] ? 0 : intval($expire['ttl']);
			if($current === $number && $ttl > 0 && in_array($type, [1,2]) ){
				$type === 1 ? self::$r->expire($key,$ttl) :  self::$r->expireAt($key,$ttl);
			}
		}
		return false;
	}

	/**
	 * 执行时间间隔限制
	 * @param  string $key key名称
	 * @param  int    $interval 间隔时间
	 * @return bool 结果
	 */
	private function run($key,$interval)
	{
		if(!self::$r->exists($key) ){
			self::$r->setex($key,self::DEFAULT_EXPIRE_TIME,time());
			return true;
		}

		$timestamp = self::$r->get($key);
		if(time() - $timestamp > $interval){
			self::$r->setex($key,self::DEFAULT_EXPIRE_TIME,time());
			return true;
		}

		return false;
	}

}
```

#### 签名验证

```php
class Auth 
{
	const SIGN_EXPIRES = 50; 

	// 验证IP
	static function checkIp(string $ip): bool
	{
		$allowIps = [ //ip白名单
			'127.0.0.1',
			'115.205.1.26', //公司
			'47.93.249.6', // 2019-8-8
			'47.97.175.19', //2019/8/20
			'47.75.91.0', //2019/8/22
		];
		return in_array($ip, $allowIps,true);
	}

	// 验证签名
	static function verifySign(array $param,string $secret)
	{
		if(isset($param['version']) ) unset($param['version']);

		if(time() - $param['timestamp'] >= self::SIGN_EXPIRES){
			return Code::EXPIRED_REQUEST;
		}
		$sign = $param['signature'];
		unset($param['signature']);
		
		return self::createSign($param,$secret) === $sign;
	}

	/**
	 * 生成签名
	 * @param  $param  传递的参数
	 * @param  $secret 秘钥secret
	 * @return string  签名
	 */
	public static function createSign(array $param,string $secret)
	{
		ksort($param);
		$str = http_build_query($param);
		return md5($str.$secret);
	}
}
```







## 其他

#### Hook实现

```php
class Ball{
	 public function down(){
	 echo  "ball is downing ";
	 //注册事件
	 Hook::add("Man");
	 Hook::add("Woman");
	 }
	 public function do(){
	 Hook::exec();
	 }
}
// 钩子的定义
class Hook{
	 private static $hooklist = null;
	 // 添加
	 public static function add($people){
	 	self::$hooklist[] = new $people();
	 }
	 // 触发事件
	 public static function exec(){
		 foreach(self::$hooklist as $addon){
		   $addon ->act();
		 }
	 }
}


// 钩子实现
class Man{
 public function act(){
 echo 'notiong111111';
 }
}
class Woman{
 public function act(){
 echo 'oh my god2222222 ';
 }
}
class Child{
 public function act(){
 echo 'oh my god333333 ';
 }
}
$ball = new Ball();
$ball ->down();
$ball ->do();
```

#### Hash算法

```php
<?php

// 一致性哈希算法
class ConsistentHashing
{
    protected $nodes = [];
    protected $position = [];
    protected $mul = 64;  // 每个节点对应64个虚拟节点

    /**
     * 把字符串转为32位符号整数
     */
    public function hash($str)
    {
        return sprintf('%u', crc32($str));
    }

    /**
     * 核心功能
     */
    public function lookup($key)
    {
        $point = $this->hash($key);

        //先取圆环上最小的一个节点,当成结果
        $node = current($this->position);

        // 循环获取相近的节点
        foreach ($this->position as $key => $val) {
            if ($point <= $key) {
                $node = $val;
                break;
            }
        }

        reset($this->position);

        return $node;
    }

    /**
     * 添加节点
     */
    public function addNode($node)
    {
        if(isset($this->nodes[$node])) return;

        // 添加节点和虚拟节点
        for ($i = 0; $i < $this->mul; $i++) {
            $pos = $this->hash($node . '-' . $i);
            $this->position[$pos] = $node;
            $this->nodes[$node][] = $pos;
        }

        // 重新排序
        $this->sortPos();
    }

    /**
     * 删除节点
     */
    public function delNode($node)
    {
        if (!isset($this->nodes[$node])) return;

        // 循环删除虚拟节点
        foreach ($this->nodes[$node] as $val) {
            unset($this->position[$val]);
        }

        // 删除节点
        unset($this->nodes[$node]);
    }

    /**
     * 排序
     */
    public function sortPos()
    {
        ksort($this->position, SORT_REGULAR);
    }
}


// 测试
$con = new ConsistentHashing();

$con->addNode('a');
$con->addNode('b');
$con->addNode('c');
$con->addNode('d');

$key1 = 'www.zhihu.com';
$key2 = 'www.baidu.com';
$key3 = 'www.google.com';

echo 'key' . $key1 . '落在' . $con->lookup($key1) . '号节点上！<br>';
echo 'key' . $key2 . '落在' . $con->lookup($key2) . '号节点上！<br>';
echo 'key' . $key3 . '落在' . $con->lookup($key3) . '号节点上！<br>';


```







#### 区块链算法实现

```php
<?php 
/**
 * 区块链相关算法
 */
class Block
{
    
    public $timestamp; //时间
   
    public $index; //索引
    
    public $data; //数据

    public $prevHash; //上一个哈希值
    
    public $hash; //当前哈希值

    public function __construct($index, $timestamp, $data, $prevHash = '')
    {
        $this->index = $index;
        $this->timestamp = $timestamp;
        $this->data = $data;
        $this->prevHash = $prevHash;
        $this->hash = $this->calculateHash();
    }
    /**
     * 加密算法
     * @return string
     */
    public function calculateHash()
    {
        return hash('sha256', $this->index . $this->prevHash . $this->timestamp . json_encode($this->data));
    }
}
/**
 * 区块链
 * Class BlockChain
 */
class BlockChain
{

    public $chain = []; // Block[]

    public function __construct()
    {
        $this->chain = [$this->createGenesisBlock()];
    }
    /**
     * 创世区块
     * @return Block
     */
    public function createGenesisBlock()
    {
        return new Block(0, '2017-01-23', 'forecho', '0');
    }
    /**
     * 获取最新的区块
     * @return Block|mixed
     */
    public function getLatestBlock()
    {
        return $this->chain[count($this->chain) - 1];
    }
    /**
     * 添加区块
     * @param Block $newBlock
     */
    public function addBlock(Block $newBlock)
    {
        $newBlock->prevHash = $this->getLatestBlock()->hash;
        $newBlock->hash = $newBlock->calculateHash();
        array_push($this->chain, $newBlock);
    }
    /**
     * 验证区块链
     * @return bool
     */
    public function isChainValid()
    {
        for ($i = 1; $i < count($this->chain); $i++) {
            $currentBlock = $this->chain[$i];
            $prevBlock = $this->chain[$i - 1];
            if ($currentBlock->hash !== $currentBlock->calculateHash()) {
                return false;
            }
            if ($currentBlock->prevHash !== $prevBlock->hash) {
                return false;
            }
        }
        return true;
    }
}
// test
$blockChain = new BlockChain();
$blockChain->addBlock(new Block(1, '2017-02-23', ['amount' => 1]));
$blockChain->addBlock(new Block(2, '2017-03-23', ['amount' => 3]));
$blockChain->addBlock(new Block(3, '2017-04-23', ['amount' => 20]));
print_r($blockChain);
echo "区块链验证通过吗？" . ($blockChain->isChainValid() ? '通过' : '失败') . PHP_EOL;
$blockChain->chain[1]->data = ['amount' => 2];
$blockChain->chain[1]->hash = $blockChain->chain[1]->calculateHash();
echo "区块链验证通过吗？" . ($blockChain->isChainValid() ? '通过' : '失败') . PHP_EOL;

```



