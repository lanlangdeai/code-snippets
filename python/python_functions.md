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

邮箱验证

```python
def check_email(email):
    """
    验证邮箱
    :param email 邮箱地址
    :return: bool 是否验证通过
    """
    return re.match(r"^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.(com|cn|net)$", email)
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



