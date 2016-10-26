# Django中常用的路径

# BASE_DIR

在setting.py中，第一个定义的全局变量就是这么一个路径：

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

这个路径定义的是django服务运行的“当前目录”。打开views.py,添加下面代码：

	from django.conf import settings
	def home(request):
	    return HttpResponse(settings.BASE_DIR)

这段代码在首页打印settings.BASE_DIR的内容，结果如下：

	/home/ubuntu/workspace/my_site

这个就是网站的根目录。

# static目录

在保存静态文件时常用这样的目录。在网站的根目录创建static文件夹，例如：

	static/
	├── assets
	│   ├── css
	│   │   └── screen.css
	│   ├── favicon.ico
	│   └── js
	│       └── main.js
	└── style
	    ├── blog.css
	    ├── grids-responsive-min.css
	    ├── monokai.css
	    └── pure-min.css

在setting.py文件中添加路径的全局变量：

	STATIC_URL = 'static/'
	
*注意：*

- 设置目录必须以“/”结尾，否则会报错
- 不能写成'/static/',这代表绝对路径的根目录下static目录

## 模板文件中引用

 	{% load staticfiles %}
	<link rel=stylesheet href="{% static "style/pure-min.css" %}">

或

	{% load staticfiles %}
	<link rel="shortcut icon" href="{% static "assets/favicon.ico" %}">

## 在代码中引用

### 绝对路径

	import os
	os.path.join( os.path.dirname(__file__), 'static').replace('\\','/')

### 相对路径

	from django.conf import settings
	def home(request):
		filename = 'abc.txt'
		
		# 方法一
		path = os.path.join('uploads', filename)
		
		# 方法二
		path = 'uploads/' + filename
		
		# 方法三
		path = settings.STATIC_URL + filename

		return HttpResponse(path)

这里建议使用“方法三”，一旦有目录发生变化，只需要修改settings.py中的全局变量即可。目录操作建议使用os.path.join方法。因此，常用的方法是：

	path = os.path.join(settings.STATIC_URL, filename).replace('\\','/')

# uploads目录

一般用来进行文件上传

# images目录

一般用来保存图片