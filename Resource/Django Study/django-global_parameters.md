Django 全局变量

# locals()

返回当前域中的全部局部变量。例如：

- views.py

		import datetime

		def test(request):
			a = 1
			b = 2
			current_date = datetime.datetime.now()
		 	return render(request, 'test.html', locals())

- test.html

		<html>
			<body>
				<font color = "blue">It is is now {{ current_date }}
				</font><br/><font color = "blue">It is is now {{ current_date | date:"Y /m /d" }}.</font>
		    </body>
		</html>

current_date是一个局部变量，通过locals()传递给test.html页面。a, b两个变量也被传递过去。

显示结果：

![](http://i.imgur.com/Z44jdUH.png)

第二行的时间显示加了一个filter.

# global()

与locals()相反，返回的是所有的全局变量。

# 全局字符串

一般，网站的名称、描述等信息都是固定的字符串，为了方便修改，我们用自定义的全局变量来保存它们。

打开settings.py,加入下面代码：

	# Personal Information
	SITE_NAME = "Barry's Blog"
	SITE_DESC = 'Personal Blog'

打开my_blog/article/views.py文件，加入下面代码：

	from django.conf import settings # 引入settings.py文件中的变量
  
  	def global_setting(request):
 		return{'SITE_NAME':settings.SITE_NAME,
 		'SITE_DESC':settings.SITE_DESC,}

或

	from django.conf import settings

	def global_setting(request):
		content = {'SITE_NAME':settings.SITE_NAME, 'SITE_DESC':settings.SITE_DESC,}

		return content

这段代码用global_setting这个函数将settings.py中我们刚才设置的全局变量拿到并返回一个字典对象。

再打开settings.py,找到TEMPLATES项，做如下修改：

![](http://i.imgur.com/48BZU9D.png)

OPTIONS.context_processors 里面有4条信息，其实每一条信息都对应一个函数，这里是设置每一个函数的返回值作为Template的全局变量。

我们的操作就是把自己定义的global_setting()的返回值作为Template的全局变量。

打开模板文件test.html，加入下面脚本：

	<html>
	    <head>
	        <title>{{ SITE_NAME }}</title>
	    </head>
	
	    <body>
	        <h1>{{ SITE_DESC }}</h1>
	    </body>
	</html>

查看最终结果：

![](http://i.imgur.com/fBGdolt.png)

## global_setting()其他实现方法

	def global_setting(request):
	      SITE_NAME = settings.SITE_NAME
	      SITE_DESC = settings.SITE_DESC
	      
	      return locals()

注意，由于locals()只能得到当前模块的局部变量，因此必须定义局部变量来转存settings中的信息。

# 查询结果设为全局变量

有一个经典的应用是博客中的标签云，打开博客时从数据库中查找出标签云数据，需要保存在全局变量中。否则，每次打开一个页面都要重复查询一次数据库。

修改global_setting():

	def global_setting(request):
	
	
	    # 标签云数据
	    _tag_list = Article.objects.values("category")
	    
	    _tag_list = [tag['category'] for tag in _tag_list]
	    
	    #print(tag_list)
	    
	    data = set(_tag_list)
	    
	    #print(data)
	    _tag_list = list(data)
	    
	    #print(_tag_list)
	    
	    return {'tag_list': _tag_list}

在html中这样写：

	{% for tag in tag_list %}
	    <li class="nav-item">
	        <a class="button-success pure-button" href="/">{{ tag }}</a> {{ data }}
	    </li>
	{% endfor %}

显示结果如下：

![](http://i.imgur.com/W7hJl50.png)

注意，这里没有采用locals()的方式，因为在复杂程序中，如果将全部局部变量都设为全局变量时，容易在html中出现变量名重复。比如，tag和data两个变量就容易和html中的局部变量冲突。因此，只需要将必要的变量设为全局变量即可。