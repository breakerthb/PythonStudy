# Practice List

----


# 第 0000 题 : 图片加文字

将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

类似于图中效果

![头像](https://raw.githubusercontent.com/breakerthb/PythonStudy/master/Resource/face.jpg)

# 第 0001 题 : 生成激活码

做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

# 第 0002 题 : Link MySQL

将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中

首先要在数据库中创建一个database: TESTDB

# 第 0003 题 : Link Redis

将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中

# 第 0004 题 : 统计字数

任一个英文的纯文本文件，统计其中的单词出现的个数。

# 第 0005 题 : 修改图片分辨率

你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

# 第 0006 题 : 统计关键词

你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

# 第 0007 题 : 统计代码数

有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

# 第 0008 题 : HTML文件正文

一个HTML文件，找出里面的**正文**。

# 第 0009 题 : HTML文件找链接

一个HTML文件，找出里面的**链接**。

# 第 0010 题 : 生成验证码

使用 Python 生成类似于下图中的**字母验证码图片**

![字母验证码](http://i.imgur.com/aVhbegV.jpg)

- [阅读资料](http://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python)

# 第 0011 题 : 过滤敏感词

敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

    北京
    程序员
    公务员
    领导
    牛比
    牛逼
    你娘
    你妈
    love
    sex
	jiangge

# 第 0012 题 : 替换敏感词

敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用星号 \* 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

# 第 0013 题 : 爬图程序

用 Python 写一个爬图片的程序

爬 [这个链接里的妹子图片 :-)](http://tieba.baidu.com/p/2166231880)

## requests库安装

<http://docs.python-requests.org/en/latest/user/install/#install>

- [参考代码](http://www.v2ex.com/t/61686 "参考代码")

# 第 0014 题 : Jason To Excel

纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

    {
    	"1":["张三",150,120,100],
    	"2":["李四",90,99,95],
    	"3":["王五",60,66,68]
    }

请将上述内容写到 student.xls 文件中，如下图所示：

![student.xls](http://i.imgur.com/nPDlpme.jpg)

## openpyxl模块安装

    $ pip install openpyxl

# 第 0015 题 : Jason To Excel

纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

    {
        "1" : "上海",
        "2" : "北京",
        "3" : "成都"
    }

请将上述内容写到 city.xls 文件中，如下图所示：

![city.xls](http://i.imgur.com/rOHbUzg.png)


# 第 0016 题 : Jason To Excel

纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

    [
    	[1, 82, 65535],
    	[20, 90, 13],
    	[26, 809, 1024]
    ]

请将上述内容写到 numbers.xls 文件中，如下图所示：

![numbers.xls](http://i.imgur.com/iuz0Pbv.png)

# 第 0017 题 : Excel To XML

将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

    <?xml version="1.0" encoding="UTF-8"?>
    <root>
    <students>
    <!--
    	学生信息表
    	"id" : [名字, 数学, 语文, 英文]
    -->
    {
    	"1" : ["张三", 150, 120, 100],
    	"2" : ["李四", 90, 99, 95],
    	"3" : ["王五", 60, 66, 68]
    }
    </students>
    </root>
    
## 安装需要模块
    
    $ sudo pip install xlrd
    $ sudo pip install lxml

- [阅读资料](http://www.cnblogs.com/skynet/archive/2013/05/06/3063245.html) 腾讯游戏开发 xml 和 Excel 相互转换

# 第 0018 题 : xls to xml

将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

    <?xmlversion="1.0" encoding="UTF-8"?>
    <root>
    <citys>
    <!--
    	城市信息
    -->
    {
    	"1" : "上海",
    	"2" : "北京",
    	"3" : "成都"
    }
    </citys>
    </root>

# 第 0019 题 : xls to xml

将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下

所示：

    <?xml version="1.0" encoding="UTF-8"?>
    <root>
    <numbers>
    <!--
    	数字信息
    -->

    [
    	[1, 82, 65535],
    	[20, 90, 13],
    	[26, 809, 1024]
    ]

    </numbers>
    </root>

# 第 0020 题

[登陆中国联通网上营业厅](http://iservice.10010.com/index_.html) 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。

# 第 0021 题

通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。

- 阅读资料 [用户密码的存储与 Python 示例](http://zhuoqiang.me/password-storage-and-python-example.html)

- 阅读资料 [Hashing Strings with Python](http://www.pythoncentral.io/hashing-strings-with-python/)

- 阅读资料 [Python's safest method to store and retrieve passwords from a database](http://stackoverflow.com/questions/2572099/pythons-safest-method-to-store-and-retrieve-passwords-from-a-database)

# 第 0022 题

iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。

# 第 0023 题

使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

[阅读资料：Python 有哪些 Web 框架](http://v2ex.com/t/151643#reply53)

- ![留言簿参考](http://i.imgur.com/VIyCZ0i.jpg)


**第 0024 题：** 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。

- ![SpringSide 版TodoList](http://i.imgur.com/NEf7zHp.jpg)

**第 0025 题：** 使用 Python 实现：对着电脑吼一声,自动打开浏览器中的默认网站。


    例如，对着笔记本电脑吼一声“百度”，浏览器自动打开百度首页。

    关键字：Speech to Text

参考思路：
1：获取电脑录音-->WAV文件
    python record wav

2：录音文件-->文本

    STT: Speech to Text

    STT API Google API

3:文本-->电脑命令

# 第 0026 题 : 图片转字符画

![图1](https://raw.githubusercontent.com/breakerthb/PythonStudy/master/Resource/ascii_dora.png)
![图2](https://raw.githubusercontent.com/breakerthb/PythonStudy/master/Resource/ascii_dora_out.png)

用python实现将图1转为图2.

通过下面命令得到图1：

    $ wget http://labfile.oss.aliyuncs.com/courses/370/ascii_dora.png

需要使用PIL库完成，安装pillow

    $ sudo apt-get update
    $ sudo apt-get install python-dev
    $ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
    $ sudo pip install pillow
    
最终命令：

    $ python main.py ascii_dora.png
    
# 第 0027 题 : 用命令行实现游戏2048

ref:<https://www.shiyanlou.com/courses/368/labs/1172/document>

# 第 0028 题 ： 用SMTP协议发邮件

查看gmail SMTP协议是否可用：

    $ nc -v -w 10 -z smtp.gmail.com 587