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







