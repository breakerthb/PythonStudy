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

# 自定义目录

	IMG_PATH = 'img/'

## 在代码中引用

### 绝对路径

	import os
	os.path.join( os.path.dirname(__file__), 'img').replace('\\','/')

### 相对路径

	from django.conf import settings
	def home(request):
		filename = 'abc.txt'
		
		# 方法一
		path = os.path.join('img', filename)
		
		# 方法二
		path = 'img/' + filename
		
		# 方法三
		path = settings.IMG_PATH + filename

		return HttpResponse(path)

这里建议使用“方法三”，一旦有目录发生变化，只需要修改settings.py中的全局变量即可。目录操作建议使用os.path.join方法。因此，常用的方法是：

	path = os.path.join(settings.IMG_PATH, filename).replace('\\','/')

