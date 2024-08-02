# PHP

## 安装







## 常用命令

```shell
# 查看PHP加载的配置文件
php -i|grep php.ini

# 查看php cli加载的配置文件
php --ini

# 查看加载的php扩展目录
php -i|grep extension_dir

# 平滑重启php-fpm
kill -USR2 16550
or
kill -USR2 `cat /usr/local/var/run/php-fpm.pid`
# USR2 平滑重启所有worker进程并重新载入配置和二进制模块


```


















## Composer 

### 镜像加速

```bash
# 取消全局配置
composer config -g --unset repos.packagist

# 全局设置
composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/

# 单独设置
composer config repo.packagist composer https://mirrors.aliyun.com/composer/


## 更多设置
# 腾讯云
composer config -g repos.packagist composer https://mirrors.cloud.tencent.com/composer/



```
### 安装依赖包
```bash
# 存在composer.json文件的情况
composer install

# 安装单独包
composer require 包名称

```



## 常用操作

### 项目中错误展示与级别设置

```php
$project_environment = getenv('PROJECT_ENVIRONMENT');
if($project_environment == 'production'){
    defined('PRO_ENV') or define('PRO_ENV', 'prod');
}elseif($project_environment == 'test'){
    defined('PRO_ENV') or define('PRO_ENV', 'test');
    ini_set('display_errors', 1);
    //开启错误和警告，严格规范开发
    error_reporting(E_ALL ^E_NOTICE);
}else{
    defined('PRO_ENV') or define('PRO_ENV', 'dev');
    ini_set('display_errors', 1);
    //开启错误和警告，严格规范开发
    error_reporting(E_ALL ^E_NOTICE);
}
```



### 跨域处理

```php
// 设置允许其他域名访问
header('Access-Control-Allow-Origin:*');  
// 设置允许的响应类型 
header('Access-Control-Allow-Methods:POST, GET');  
// 设置允许的响应头 
header('Access-Control-Allow-Headers:x-requested-with,content-type'); 


$origin = isset($_SERVER['HTTP_ORIGIN'])? $_SERVER['HTTP_ORIGIN'] : '';
$allow_origin = array(
    'http://domain1',
    'http://domain2',
    'https://domain3',
);
if(in_array($origin, $allow_origin)){
    header('Access-Control-Allow-Origin:'.$origin);
    header('Access-Control-Allow-Methods:POST,GET');
    header('Access-Control-Allow-Headers:x-requested-with,content-type');
}
```





## 常见问题

1.本地不存在memcached的解决方案

```php
<?php
// WARNING: only for windows  no memcache dll, the function connect is CHANGED
/**
 * PHP memcached client class
 *
 * For build develop environment in windows using memcached.
 *
 * @package     memcached-client
 * @copyright   Copyright 2013-2014, Fwolf
 * @author      Fwolf <fwolf.aide+memcached-client@gmail.com>
 * @license     http://www.gnu.org/licenses/lgpl.html LGPL v3
 * @since       2013-01-18
 * @version     1.1.0
 */
class Memcache extends Memcached {}
class Memcached
{
    // Predefined Constants
    // See: http://php.net/manual/en/memcached.constants.php

    // Defined in php_memcached.c
    const OPT_COMPRESSION = -1001;
    const OPT_SERIALIZER = -1003;

    // enum memcached_serializer in php_memcached
    const SERIALIZER_PHP = 1;
    const SERIALIZER_IGBINARY = 2;
    const SERIALIZER_JSON = 3;

    // Defined in php_memcached.c
    const OPT_PREFIX_KEY = -1002;

    // enum memcached_behavior_t in libmemcached
    const OPT_HASH = 2;     //MEMCACHED_BEHAVIOR_HASH

    // enum memcached_hash_t in libmemcached
    const HASH_DEFAULT = 0;
    const HASH_MD5 = 1;
    const HASH_CRC = 2;
    const HASH_FNV1_64 = 3;
    const HASH_FNV1A_64 = 4;
    const HASH_FNV1_32 = 5;
    const HASH_FNV1A_32 = 6;
    const HASH_HSIEH = 7;
    const HASH_MURMUR = 8;

    // enum memcached_behavior_t in libmemcached
    const OPT_DISTRIBUTION = 9;     // MEMCACHED_BEHAVIOR_DISTRIBUTION

    // enum memcached_server_distribution_t in libmemcached
    const DISTRIBUTION_MODULA = 0;
    const DISTRIBUTION_CONSISTENT = 1;

    // enum memcached_behavior_t in libmemcached
    const OPT_LIBKETAMA_COMPATIBLE = 16;    // MEMCACHED_BEHAVIOR_KETAMA_WEIGHTED
    const OPT_BUFFER_WRITES = 10;           // MEMCACHED_BEHAVIOR_BUFFER_REQUESTS
    const OPT_BINARY_PROTOCOL = 18;         // MEMCACHED_BEHAVIOR_BINARY_PROTOCOL
    const OPT_NO_BLOCK = 0;                 // MEMCACHED_BEHAVIOR_NO_BLOCK
    const OPT_TCP_NODELAY = 1;              // MEMCACHED_BEHAVIOR_TCP_NODELAY
    const OPT_SOCKET_SEND_SIZE = 4;         // MEMCACHED_BEHAVIOR_SOCKET_SEND_SIZE
    const OPT_SOCKET_RECV_SIZE = 5;         // MEMCACHED_BEHAVIOR_SOCKET_RECV_SIZE
    const OPT_CONNECT_TIMEOUT = 14;         // MEMCACHED_BEHAVIOR_CONNECT_TIMEOUT
    const OPT_RETRY_TIMEOUT = 15;           // MEMCACHED_BEHAVIOR_RETRY_TIMEOUT
    const OPT_SEND_TIMEOUT = 19;            // MEMCACHED_BEHAVIOR_SND_TIMEOUT
    const OPT_RECV_TIMEOUT = 20;            // MEMCACHED_BEHAVIOR_RCV_TIMEOUT
    const OPT_POLL_TIMEOUT = 8;             // MEMCACHED_BEHAVIOR_POLL_TIMEOUT
    const OPT_CACHE_LOOKUPS = 6;            // MEMCACHED_BEHAVIOR_CACHE_LOOKUPS
    const OPT_SERVER_FAILURE_LIMIT = 21;    // MEMCACHED_BEHAVIOR_SERVER_FAILURE_LIMIT

    // In php_memcached config, define HAVE_MEMCACHED_IGBINARY default 1,
    // then use ifdef define HAVE_IGBINARY to 1.
    const HAVE_IGBINARY = 1;
    // In php_memcached config, define HAVE_JSON_API default 1,
    // then use ifdef define HAVE_JSON to 1.
    const HAVE_JSON = 1;

    // Defined in php_memcached.c, (1<<0)
    const GET_PRESERVE_ORDER = 1;

    // enum memcached_return_t in libmemcached
    const RES_SUCCESS = 0;                  // MEMCACHED_SUCCESS
    const RES_FAILURE = 1;                  // MEMCACHED_FAILURE
    const RES_HOST_LOOKUP_FAILURE = 2;      // MEMCACHED_HOST_LOOKUP_FAILURE
    const RES_UNKNOWN_READ_FAILURE = 7;     // MEMCACHED_UNKNOWN_READ_FAILURE
    const RES_PROTOCOL_ERROR = 8;           // MEMCACHED_PROTOCOL_ERROR
    const RES_CLIENT_ERROR = 9;             // MEMCACHED_CLIENT_ERROR
    const RES_SERVER_ERROR = 10;            // MEMCACHED_SERVER_ERROR
    const RES_WRITE_FAILURE = 5;            // MEMCACHED_WRITE_FAILURE
    const RES_DATA_EXISTS = 12;             // MEMCACHED_DATA_EXISTS
    const RES_NOTSTORED = 14;               // MEMCACHED_NOTSTORED
    const RES_NOTFOUND = 16;                // MEMCACHED_NOTFOUND
    const RES_PARTIAL_READ = 18;            // MEMCACHED_PARTIAL_READ
    const RES_SOME_ERRORS = 19;             // MEMCACHED_SOME_ERRORS
    const RES_NO_SERVERS = 20;              // MEMCACHED_NO_SERVERS
    const RES_END = 21;                     // MEMCACHED_END
    const RES_ERRNO = 26;                   // MEMCACHED_ERRNO
    const RES_BUFFERED = 32;                // MEMCACHED_BUFFERED
    const RES_TIMEOUT = 31;                 // MEMCACHED_TIMEOUT
    const RES_BAD_KEY_PROVIDED = 33;        // MEMCACHED_BAD_KEY_PROVIDED
    const RES_CONNECTION_SOCKET_CREATE_FAILURE = 11;    // MEMCACHED_CONNECTION_SOCKET_CREATE_FAILURE

    // Defined in php_memcached.c
    const RES_PAYLOAD_FAILURE = -1001;


    /**
     * Dummy option array
     *
     * @var array
     */
    protected $option = array(
        Memcached::OPT_COMPRESSION  => true,
        Memcached::OPT_SERIALIZER   => Memcached::SERIALIZER_PHP,
        Memcached::OPT_PREFIX_KEY   => '',
        Memcached::OPT_HASH         => Memcached::HASH_DEFAULT,
        Memcached::OPT_DISTRIBUTION => Memcached::DISTRIBUTION_MODULA,
        Memcached::OPT_LIBKETAMA_COMPATIBLE => false,
        Memcached::OPT_BUFFER_WRITES    => false,
        Memcached::OPT_BINARY_PROTOCOL  => false,
        Memcached::OPT_NO_BLOCK     => false,
        Memcached::OPT_TCP_NODELAY  => false,

        // This two is a value by guess
        Memcached::OPT_SOCKET_SEND_SIZE => 32767,
        Memcached::OPT_SOCKET_RECV_SIZE => 65535,

        Memcached::OPT_CONNECT_TIMEOUT  => 1000,
        Memcached::OPT_RETRY_TIMEOUT    => 0,
        Memcached::OPT_SEND_TIMEOUT     => 0,
        Memcached::OPT_RECV_TIMEOUT     => 0,
        Memcached::OPT_POLL_TIMEOUT     => 1000,
        Memcached::OPT_CACHE_LOOKUPS    => false,
        Memcached::OPT_SERVER_FAILURE_LIMIT => 0,
    );


    /**
     * Last result code
     *
     * @var int
     */
    protected $resultCode = 0;


    /**
     * Last result message
     *
     * @var string
     */
    protected $resultMessage = '';


    /**
     * Server list array/pool
     *
     * I added array index.
     *
     * array (
     *  host:port:weight => array(
     *      host,
     *      port,
     *      weight,
     *  )
     * )
     *
     * @var array
     */
    protected $server = array();


    /**
     * Socket connect handle
     *
     * Point to last successful connect, ignore others
     * @var resource
     */
    protected $socket = null;


    /**
     * Add a serer to the server pool
     *
     * @param   string  $host
     * @param   int     $port
     * @param   int     $weight
     * @return  boolean
     */
    public function addServer($host, $port = 11211, $weight = 0, $timeout=1)
    {
        $key = $this->getServerKey($host, $port, $weight);
        if (isset($this->server[$key])) {
            // Dup
            $this->resultCode = Memcached::RES_FAILURE;
            $this->resultMessage = 'Server duplicate.';
            return false;

        } else {
            $this->server[$key] = array(
                'host'  => $host,
                'port'  => $port,
                'weight'    => $weight,
                'timeout' => $timeout,
            );

            $this->connect();
            return true;
        }
    }


    /**
     * Add multiple servers to the server pool
     *
     * @param   array   $servers
     * @return  boolean
     */
    public function addServers($servers)
    {
    
        foreach ((array)$servers as $svr) {
            $host = array_shift($svr);

            $port = array_shift($svr);
            if (is_null($port)) {
                $port = 11211;
            }

            $weight = array_shift($svr);
            if (is_null($weight)) {
                $weight = 0;
            }

            $timeout = array_shift($svr); {
                if (is_null($timeout)) {
                    $timeout = 1;
                }
            }
            $this->addServer($host, $port, $weight, $timeout);
        }

        return true;
    }


    /**
     * Connect to memcached server
     *
     * @return  boolean
     */
    protected function connect()
    {
       // return true;
        $rs = false;
        foreach ((array)$this->server as $svr) {
            $error = 0;
            $errstr = '';
            $st = time();
            $rs = @fsockopen($svr['host'], $svr['port'], $error, $errstr, 1);
           // var_dump($rs);exit;

            if ($rs) {
                $this->socket = $rs;
            } else {
                $key = $this->getServerKey(
                    $svr['host'],
                    $svr['port'],
                    $svr['weight']
                );
                $s = "Connect to $key error:" . PHP_EOL .
                    "    [$error] $errstr";
                error_log($s);
            }
        }

        if (is_null($this->socket)) {
            $this->resultCode = Memcached::RES_FAILURE;
            $this->resultMessage = 'No server avaliable.';
            return false;

        } else {
            $this->resultCode = Memcached::RES_SUCCESS;
            $this->resultMessage = '';
            return true;
        }
    }


    /**
     * Delete an item
     *
     * @param   string  $key
     * @param   int     $time       Ignored
     * @return  boolean
     */
    public function delete($key, $time = 0)
    {
        $keyString = $this->getKey($key);
        $this->writeSocket("delete $keyString");

        $s = $this->readSocket();
        if ('DELETED' == $s) {
            $this->resultCode = Memcached::RES_SUCCESS;
            $this->resultMessage = '';
            return true;

        } else {
            $this->resultCode = Memcached::RES_NOTFOUND;
            $this->resultMessage = 'Delete fail, key not exists.';
            return false;
        }
    }


    /**
     * Retrieve an item
     *
     * @param   string  $key
     * @param   callable    $cache_cb       Ignored
     * @param   float   $cas_token          Ignored
     * @return  mixed
     */
    public function get($key, $cache_cb = null, $cas_token = null)
    {
        $keyString = $this->getKey($key);
        $this->writeSocket("get $keyString");

        $s = $this->readSocket();

        if (is_null($s) || 'VALUE' != substr($s, 0, 5)) {
            $this->resultCode = Memcached::RES_FAILURE;
            $this->resultMessage = 'Get fail.';
            return false;

        } else {
            $s_result = '';
            $s = $this->readSocket();
            while ('END' != $s) {
                $s_result .= $s;
                $s = $this->readSocket();
            }
            $this->resultCode = Memcached::RES_SUCCESS;
            $this->resultMessage = '';

            return unserialize($s_result);
        }
    }


    /**
     * Get item key
     *
     * @param   string  $key
     * @return  string
     */
    public function getKey($key)
    {
        return addslashes($this->option[Memcached::OPT_PREFIX_KEY]) . $key;
    }


    /**
     * Get a memcached option value
     *
     * @param   int     $option
     * @return  mixed
     */
    public function getOption($option)
    {
        if (isset($this->option[$option])) {
            $this->resultCode = Memcached::RES_SUCCESS;
            $this->resultMessage = '';
            return $this->option[$option];

        } else {
            $this->resultCode = Memcached::RES_FAILURE;
            $this->resultMessage = 'Option not seted.';
            return false;
        }
    }


    /**
     * Return the result code of the last operation
     *
     * @return  int
     */
    public function getResultCode()
    {
        return $this->resultCode;
    }


    /**
     * Return the message describing the result of the last opteration
     *
     * @return  string
     */
    public function getResultMessage()
    {
        return $this->resultMessage;
    }


    /**
     * Get key of server array
     *
     * @param   string  $host
     * @param   int     $port
     * @param   int     $weight
     * @return  string
     */
    protected function getServerKey($host, $port = 11211, $weight = 0)
    {
        return "$host:$port:$weight";
    }


    /**
     * Get list array of servers
     *
     * @see     $server
     * @return  array
     */
    public function getServerList()
    {
        return $this->server;
    }


    /**
     * Read from socket
     *
     * @return  string|null
     */
    protected function readSocket()
    {
        if (is_null($this->socket)) {
            return null;
        }

        return trim(fgets($this->socket));
    }




    /**
     * Store an item
     *
     * @param   string  $key
     * @param   mixed   $val
     * @param   int     $expt
     * @return  boolean
     */
    public function set($key, $val, $expt = 0)
    {
        $valueString = serialize($val);
        $keyString = $this->getKey($key);

        $this->writeSocket(
            "set $keyString 0 $expt " . strlen($valueString)
        );
        $s = $this->writeSocket($valueString, true);

        if ('STORED' == $s) {
            $this->resultCode = Memcached::RES_SUCCESS;
            $this->resultMessage = '';
            return true;

        } else {
            $this->resultCode = Memcached::RES_FAILURE;
            $this->resultMessage = 'Set fail.';
            return false;
        }
    }


    /**
     * Set a memcached option
     *
     * @param   int     $option
     * @param   mixed   $value
     * @return  boolean
     */
    public function setOption($option, $value)
    {
        $this->option[$option] = $value;
        return true;
    }


    /**
     * Set memcached options
     *
     * @param   array   $options
     * @return  bollean
     */
    public function setOptions($options)
    {
        $this->option = array_merge($this->option, $options);
        return true;
    }
    /**
     * Write data to socket
     *
     * @param   string  $cmd
     * @param   boolean $result     Need result/response
     * @return  mixed
     */
    protected function writeSocket($cmd, $result = false)
    {
        if (is_null($this->socket)) {
            return false;
        }

        fwrite($this->socket, $cmd . "\r\n");

        if (true == $result) {
            return $this->readSocket();
        }

        return true;
    }
}

```

