
# 标准GET方式写法

通过 **/add/?a=4&b=5** 这样的方式实现

新建工程和应用

	$ django-admin.py startproject calculate
	$ cd calculate
	$ python manage.py startapp calc

我们修改一下 calc/views.py文件

	from django.shortcuts import render
	from django.http import HttpResponse
	 
	def add(request):
	    a = request.GET['a']
	    b = request.GET['b']
	    # b = request.GET.get('b', 0)
	    c = int(a)+int(b)
	    return HttpResponse(str(c))

## request.GET

request.GET类似于一个字典，更好的办法是用 request.GET.get('b', 0) 当没有传递 b 的时候默认 a 为 0

接着修改 calculate/urls.py 文件，添加一个网址来对应我们刚才新建的视图函数。

Django 1.7.x 及以下的同学可能看到的是这样的：

	from django.conf.urls import patterns, include, url
	 
	from django.contrib import admin
	admin.autodiscover()
	 
	urlpatterns = patterns('',
	    # Examples:
	    url(r'^add/$', 'calc.views.add', name='add'), # 注意修改了这一行
	    # url(r'^blog/', include('blog.urls')),
	 
	    url(r'^admin/', include(admin.site.urls)),
	)

Django 1.8.x及以上，Django 官方鼓励（或说要求）先引入，再使用，低版本的 Django 也可以这样用：

	from django.conf.urls import url
	from django.contrib import admin
	from calc import views as calc_views
	 	 
	urlpatterns = [
	    url(r'^add/', calc_views.add, name='add'),  # 注意修改了这一行
	    url(r'^admin/', admin.site.urls),
	]

运行服务器，访问

	$ python manage.py runserver

打开网址：http://127.0.0.1:8000/add/ 就可以看到

![](http://i.imgur.com/2VUcltn.png)

这是因为我们并没有传值进去，我们在后面加上 ?a=4&b=5，即访问 <http://127.0.0.1:8000/add/?a=4&b=5>

![](http://i.imgur.com/GMbPiHv.png)

## 优雅的GET写法

采用 /add/3/4/ 这样的网址的方式

我们接着修改 calc/views.py文件，添加一个add2 函数

	def add2(request, a, b):
	    c = int(a) + int(b)
	    return HttpResponse(str(a) + '+' + str(b) + '=' + str(c))

接着修改 calculate/urls.py 文件，再添加一个新的 url

Django 1.7.x 及以下：

    url(r'^add/(\d+)/(\d+)/$', 'calc.views.add2', name='add2'),

Django 1.8.x 及以上：

    url(r'^add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),

**注意：**这条URL要放在第一个解析的位置

我们可以看到网址中多了 (\d+), 正则表达式中 \d 代表一个数字，+ 代表一个或多个前面的字符，写在一起 \d+ 就是一个或多个数字，用括号括起来的意思是保存为一个子组（更多知识请参见 Python 正则表达式），每一个子组将作为一个参数，被 views.py 中的对应视图函数接收。

访问 <http://127.0.0.1:8000/add/456/789/> 可见下面页面：

![](http://i.imgur.com/wUeU8Oj.png)

**总结**:所谓优雅的方式就是直接将两个参数传入views中接口的参数中。


# urls.py中使用正则表达式的写法

    url(r'^(?P<id>\d+)/$', 'article_views.detail', name='detail'),

 '^(?P<id>\d+)/$'正则表达式匹配后取出id, 然后将id传送到article_views.detail作为函数参数, 然后通过get方法获取对应的数据库对象, 然后对对应的模板进行渲染, 发送到浏览器中.
 
 如：
 
 <https://django-workspace-breakerthb.c9users.io/3/>这个URL将会被取出3之后送给detail作为参数

views.py中这样写:

	def detail(request):
		_id=request.GET['id']
		return HttpResponse("id is : " + str(_id))

# url 中的 name 使用

再来看一下 urls.py 中的代码

	from django.conf.urls import url
	from django.contrib import admin
	from calc import views as calc_views
	 
	urlpatterns = [
	    url(r'^add/', calc_views.add, name='add'),
	    url(r'^add2/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
	    url(r'^admin/', admin.site.urls),
	]

url(r'^add/$', calc_views.add, name='add'), 这里的 name='add' 是用来干什么的呢？

我们在开发的时候，刚开始想用的是 /add2/4/5/，后来需求发生变化，比如我们又想改成 /4_add_5/这样的格式，但是我们在网页中，代码中很多地方都写死的是 

	<a href="/add2/4/5/">计算 4+5</a>

这样就导致当我们改了 urls.py 后，对应的模板，视图中的跳转，以及 models.py 中都要改。

那么有没有更优雅的方式来解决这个问题呢？

## 1. 用 Python 代码获取对应的网址

我们在终端上输入(推荐安装 bpython, 这样Django会用 bpython的 shell)

	python manage.py shell
	>>> from django.core.urlresolvers import reverse
	>>> reverse('add2', args=(4,5))
	u'/add2/4/5/'
	>>> reverse('add2', args=(444,555))
	u'/add2/444/555/'

reverse 接收 url 中的 name 作为第一个参数，我们在代码中就可以通过 reverse() 来获取对应的网址（这个网址可以用来跳转，也可以用来计算相关页面的地址），只要对应的 url 的name不改，就不用改代码中的网址。

在网页模板中也是一样，可以很方便的使用。

	不带参数的：
	{% url 'name' %}

	带参数的：参数可以是变量名
	{% url 'name' 参数 %}
 
例如：

	<a href="{% url 'add2' 4 5 %}">link</a>

上面的代码渲染成最终的页面是

	<a href="/add2/4/5/">link</a>

这样就可以通过 {% url 'add2' 4 5 %} 获取到对应的网址 /add2/4/5/

当 urls.py 进行更改，前提是不改 name（这个参数设定好后不要轻易改），获取的网址也会动态地跟着变，比如改成：

	url(r'^new_add/(\d+)/(\d+)/$', 'calc.views.add2', name='add2'),


注意看重点 add2 变成了 new_add，但是后面的 name='add2' 没改，这时 {% url 'add2' 4 5 %} 就会渲染对应的网址成 /new_add/4/5/

reverse 函数也是一样，获取的时候会跟着变成新的网址，这样，在想改网址时只需要改 urls.py 中的正则表达式（url 参数第一部分），其它地方都“自动”跟着变了。

另外，如何让以前的 /add2/3/4/自动跳转到新的网址呢？要知道Django不会帮你做这个，这个需要自己来写一个跳转方法：

具体思路是，在 views.py 写一个跳转的函数：

	from django.http import HttpResponseRedirect
	from django.core.urlresolvers import reverse
	 	 
	def old_add2_redirect(request, a, b):
	    return HttpResponseRedirect(
	        reverse('add2', args=(a, b))
	    )

urls.py中：

    url(r'^add2/(\d+)/(\d+)/$', calc_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),

这样，假如用户收藏夹中有 /add2/4/5/ ，访问时就会自动跳转到新的 /new_add/4/5/ 了

**总结：**

在html页码的{% %}标签中，只需要关注“name”和n个参数，从而保证无论views.py有任何变化都不用修改html页面。

例如：

	# a.html
	<a href="{% url "detail" post.id %}">AAAA</a>
