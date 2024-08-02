# python相关函数



## 函数

### 验证

#### 手机号验证

```python
def check_phone(phone):
    """
    验证手机号
    :param phone: 手机号
    :return: bool 是否验证通过
    """
    return re.match(r'1[345789]\d{9}$', phone)
```

#### 邮箱验证

```python
def check_email(email):
    """
    验证邮箱
    :param email 邮箱地址
    :return: bool 是否验证通过
    """
    return re.match(r"^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.(com|cn|net)$", email)
```



### 获取时间相关

#### 时间戳转字符串

```python
def timestamp_to_str(ts: int, fmt: str = '%Y-%m-%d %H:%M:%S') -> str:
    """时间戳转字符串"""
    timestamp = time.localtime(ts)
    formated_string = time.strftime(fmt, timestamp)
    return formated_string
```

#### 字符串转时间戳

```python
def str_to_timestamp(today_date, fmt: str = '%Y-%m-%d %H:%M:%S') -> int:
    """时间字符串转时间戳"""
    import time
    today_arr = time.strptime(today_date, fmt)
    return int(time.mktime(today_arr))
```

#### 时间格式转换

```python
def format_date(publish_date: str) -> str:
    """时间格式替换"""
    return re.sub(r'(\d+)-(\d+)', r'\1_\2', publish_date)
```

#### 获取当前开始于结束日期时间

```python
from datetime import date, timedelta, datetime, time
def get_today_start_and_end():
    """获取当日的开始时间与结束时间"""
    pub_date = date.today()
    min_pub_date_time = datetime.combine(pub_date, time.min)
    max_pub_date_time = datetime.combine(pub_date, time.max)
    return min_pub_date_time, max_pub_date_time
```

#### 获取时间戳(昨天,今天,明天的开始与结束)

```python
def get_timestamps():
    """获取时间戳(昨天,今天,明天的开始与结束)"""
    import time
    import datetime

    # 今天日期
    today = datetime.date.today()

    # 昨天时间
    yesterday = today - datetime.timedelta(days=1)

    # 明天时间
    tomorrow = today + datetime.timedelta(days=1)
    # 后天
    acquire = today + datetime.timedelta(days=2)

    # 昨天开始时间戳
    yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))

    # 昨天结束时间戳
    yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1

    # 今天开始时间戳
    today_start_time = yesterday_end_time + 1

    # 今天结束时间戳
    today_end_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1

    # 明天开始时间戳
    tomorrow_start_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d')))

    # 明天结束时间戳
    tomorrow_end_time = int(time.mktime(time.strptime(str(acquire), '%Y-%m-%d'))) - 1
    return dict(
        today_start_time=today_start_time,
        today_end_time=today_end_time,
        yesterday_start_time=yesterday_start_time,
        yesterday_end_time=yesterday_end_time,
        tomorrow_start_time=tomorrow_start_time,
        tomorrow_end_time=tomorrow_end_time
    )
```



#### 获取指定范围的日期列表

```python
import datetime

def get_date_list(start_date, end_date):
    date_list = []
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    date_list.append(start_date.strftime('%Y-%m-%d'))
    while start_date < end_date:
        start_date += datetime.timedelta(days=1)
        date_list.append(start_date.strftime('%Y-%m-%d'))
    return date_list
```









## 类库

#### 实现布隆过滤器

```python
import random

import mmh3
import redis

# pip install mmh3
class BloomFilter(object):
    def __init__(self, bf_key, bit_size=10000, hash_count=3, start_seed=41):
        self.bit_size = bit_size
        self.hash_count = hash_count
        self.start_seed = start_seed
        self.client = redis.StrictRedis()
        self.bf_key = bf_key

    def add(self, data):
        bit_points = self._get_hash_points(data)
        for index in bit_points:
            self.client.setbit(self.bf_key, index, 1)

    def madd(self, m_data):
        if isinstance(m_data, list):
            for data in m_data:
                self.add(data)
        else:
            self.add(m_data)

    def exists(self, data):
        bit_points = self._get_hash_points(data)
        result = [
            self.client.getbit(self.bf_key, index) for index in bit_points
        ]
        return all(result)

    def mexists(self, m_data):
        result = {}
        if isinstance(m_data, list):
            for data in m_data:
                result[data] = self.exists(data)
        else:
            result[m_data] = self.exists[m_data]
        return result

    def _get_hash_points(self, data):
        return [
            mmh3.hash(data, index) % self.bit_size
            for index in range(self.start_seed, self.start_seed +
                               self.hash_count)
            ]


number_name = 'numbers2'
bool_filter = BloomFilter(number_name)

# for i in range(1, 100):
#     i = str(i)
#     print('添加元素:', i)
#     bool_filter.add(i)

for j in range(0, 30):
    j = str(j)
    print('*'*30)
    id = str(random.randint(1, 1000))

    is_exists = bool_filter.exists(id)
    print('随机元素:', id, ' 是否存在:', is_exists)
```



