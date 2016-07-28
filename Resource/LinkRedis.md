# Redis安装

[Redis安装](https://www.zybuluo.com/breakerthb/note/450244)

# 安装Python的Redis模块

<https://pypi.python.org/pypi/redis/2.10.5>

## 源码安装

<http://pypi.python.org/pypi?%3Aaction=search&term=redis&submit=search>

找到redis-py-2.2.1.tar.gz


	$ tar xvzf redis-py-2.2.1.tar.gz

进入目录：

	$ python setup.py install

## Pip安装

	$ sudo pip install redis
	$ sudo easy_install redis

# 常用命令

打开Python解释器

## 建立连接

	>>> import redis
	>>> r = redis.Redis(host='localhost', port=6379, db=0)
	# 如果设置了密码，就加上password=密码
	
## 添加数据

	>>> r.set('foo', 'bar')   # 或者写成 r['foo'] = 'bar'
	True

## 查询数据

	>>> r.get('foo')   
	'bar'

	>>> r.dbsize()   #库里有多少key，多少条数据
	0

	>>> r.exists('chang')  #看是否存在这个键值
	False

	>>> a = r.get('chang')
	>>> a    # 因为是Noen对象，什么也不显示！
	
	>>> r.keys()   # 列出所有键值。（这时候已经存了4个了）
	['aaa', 'test', 'bbb', 'key1']

	>>> dir(a)  
	['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

## 删除数据

	>>> r.delete('foo')
	True

	>>> r.flushdb()   #删除当前数据库的所有数据
	True

## 保存数据 

	>>> r.save()   #强行把数据库保存到硬盘。保存时阻塞
	True
 
# 原作者博客

<https://github.com/andymccurdy/redis-py>

 