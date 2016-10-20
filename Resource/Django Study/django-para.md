----

- 列表，字典，类的实例的使用
- 循环：迭代显示列表，字典等中的内容
- 条件判断：判断是否显示该内容，比如判断是手机访问，还是电脑访问，给出不一样的代码。
- 标签：for，if 这样的功能都是标签。
- 过滤器：管道符号后面的功能，比如{{ var|length }}，求变量长度的 length 就是一个过滤器。

如果需要将一个或多个变量共享给多个网页或者所有网页使用，比如在网页上显示来访者的IP，这个可以使用 Django 上下文渲染器 来做。

# 1. 字符串传递

显示一个基本的字符串在网页上

- views.py

		# -*- coding: utf-8 -*-
		from django.shortcuts import render
		 		 
		def home(request):
		    string = u"Create a new web site"
		    return render(request, 'home.html', {'string': string})

在视图中我们传递了一个字符串名称是 string 到模板 home.html，在模板中这样使用它：

- home.html

	    {{ string }}

![](http://i.imgur.com/mtvryKa.png)

# 2. for循环显示List内容

- views.py

		def home(request):
		    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
		    return render(request, 'home.html', {'TutorialList': TutorialList})

在视图中我们传递了一个List到模板 home.html，在模板中这样使用它：

- home.html

    	List：
    	{% for i in TutorialList %}
    	{{ i }}
    	{% endfor %}

for 循环要有一个结束标记，上面的代码假如我们对应的是首页的网址（自己修改urls.py），显示在网页上就是：

![QQ20150511-4@2x.png](http://www.ziqiangxuetang.com/media/uploads/images/QQ20150511-4_20150511212701_605.png)

*PS*：一般的变量之类的用 *{{ }}（变量）*，功能类的，比如循环，条件判断是用 *{%  %}（标签）*

变量会原封不动地显示在页面上，标签会被渲染成另外一种形式。

# 3. 显示字典中内容

- views.py

    	def home(request):
    	    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    	    return render(request, 'home.html', {'info_dict': info_dict})

- home.html

    	【站点】：{{ info_dict.site }} 【内容】：{{ info_dict.content }}

在模板中取字典的键是用点info_dict.site，而不是Python中的 info_dict['site']，效果如下：

![QQ20150511-6@2x.png](http://www.ziqiangxuetang.com/media/uploads/images/QQ20150511-6_20150511214627_734.png)

还可以这样遍历字典：

	{% for key, value in info_dict.items %}
	    {{ key }}: {{ value }}
	{% endfor %}

其实就是遍历这样一个 List:  [('content', u'自强学堂'), ('site', u'各种IT技术教程')]

![QQ20150511-7@2x.png](http://www.ziqiangxuetang.com/media/uploads/images/QQ20150511-7_20150511215246_400.png)

# 4. 条件判断和 for 循环的详细操作

- views.py

    	def home(request):
        		List = map(str, range(100))# 一个长度为100的 List
        		return render(request, 'home.html', {'List': List})

假如我们想用逗号将这些元素连接起来：

- home.html

    	{% for item in List %}
    	    {{ item }}, 
    	{% endfor %}

效果如下：

QQ20150512-1@2x.png

我们会发现最后一个元素后面也有一个逗号，这样肯定不爽，如果判断是不是遍历到了最后一个元素了呢？

用变量 forloop.last 这个变量，如果是最后一项其为真，否则为假，更改如下：

    {% for item in List %}
        {{ item }}{% if not forloop.last%},{% endif %} 
    {% endfor %}

![QQ20150512-1@2x.png](http://www.ziqiangxuetang.com/media/uploads/images/QQ20150512-1_20150512200801_668.png)

在for循环中还有很多有用的东西，如下：

	变量	描述
	forloop.counter	索引从 1 开始算
	forloop.counter0	索引从 0 开始算
	forloop.revcounter	索引从最大长度到 1
	forloop.revcounter0	索引从最大长度到 0
	forloop.first	当遍历的元素为第一项时为真
	forloop.last	当遍历的元素为最后一项时为真
	forloop.parentloop	用在嵌套的 for 循环中，获取上一层 for 循环的 forloop

当列表中可能为空值时用 for  empty

	<ul>
	{% for athlete in athlete_list %}
	    <li>{{ athlete.name }}</li>
	{% empty %}
	    <li>抱歉，列表为空</li>
	{% endfor %}
	</ul>

# 5. 模板上得到视图对应的网址(常用方法)

	# views.py
	def add(request, a, b):
	    c = int(a) + int(b)
	    return HttpResponse(str(c))
 
 	# urls.py
	urlpatterns = patterns('',
	    url(r'^add/(\d+)/(\d+)/$', 'app.views.add', name='add'),
	)
 
 	# template html
	{% url 'add' 4 5 %}

这样网址上就会显示出：/add/4/5/ 这个网址，假如我们以后修改 urls.py 中的 

	url(r'^add/(\d+)/(\d+)/$', 'app_views.add', name='add')

改成：

	url(r'^jiafa/(\d+)/(\d+)/$', 'app_views.add', name='add')

这样，我们不需要再次修改模板，当再次访问的时候，网址会自动变成 /jiafa/4/5/


注意：如果是 Django 1.4 的话，需要在模板开头加上 {% load url from future %} (如果有 extends 的话，加在 extends 下面）

还可以使用 as 语句将内容取别名（相当于定义一个变量），多次使用（但视图名称到网址转换只进行了一次）

	{% url 'some-url-name' arg arg2 as the_url %}
	 
	<a href="{{ the_url }}">链接到：{{ the_url }}</a>

# 6. 模板中的逻辑操作：

==, !=, >=, <=, >, < 这些比较都可以在模板中使用，比如：

	{% if var >= 90 %}
	成绩优秀，自强学堂你没少去吧！学得不错
	{% elif var >= 80 %}
	成绩良好
	{% elif var >= 70 %}
	成绩一般
	{% elif var >= 60 %}
	需要努力
	{% else %}
	不及格啊，大哥！多去自强学堂学习啊！
	{% endif %}

and, or, not, in, not in 也可以在模板中使用

假如我们判断 num 是不是在 0 到 100 之间：

	{% if num <= 100 and num >= 0 %}
	num在0到100之间
	{% else %}
	数值不在范围之内！
	{% endif %}
	
	假如我们判断 'ziqiangxuetang' 在不在一个列表变量 List 中：
	{% if 'ziqiangxuetang' in List %}
	自强学堂在名单中
	{% endif %}

# 7. 模板中获取当前网址，当前用户等：

如果不是在 views.py 中用的 render 函数，是 render_to_response 的话，需要将 request 加入到[上下文渲染器](http://www.ziqiangxuetang.com/django/django-context-processors.html)

Django 1.8 及以后 修改 settings.py 

	TEMPLATES = [
	    {
	        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	        'DIRS': [],
	        'APP_DIRS': True,
	        'OPTIONS': {
	            'context_processors': [
	                ...
	                'django.template.context_processors.request',
	                ...
	            ],
	        },
	    },
]

Django 1.7 及以前 修改 settings.py：

如果没有 TEMPLATE_CONTEXT_PROCESSORS 请自行添加下列默认值：

	TEMPLATE_CONTEXT_PROCESSORS = (
	    "django.contrib.auth.context_processors.auth",
	    "django.core.context_processors.debug",
	    "django.core.context_processors.i18n",
	    "django.core.context_processors.media",
	    "django.core.context_processors.static",
	    "django.core.context_processors.tz",
	    "django.contrib.messages.context_processors.messages",
	)

然后再加上 django.core.context_processors.request
TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    "django.core.context_processors.request",
    ...
)

然后在 模板中我们就可以用 request 了。

## 1.获取当前用户：

	{{ request.user }}

如果登陆就显示内容，不登陆就不显示内容：

	{% if request.user.is_authenticated %}
	    {{ request.user.username }}，您好！
	{% else %}
	    请登陆，这里放登陆链接
	{% endif %}

## 2.获取当前网址：

	{{ request.path }}

## 3. 获取当前 GET 参数：

	{{ request.GET.urlencode }}

合并到一起用的一个例子：

	<a href="{{ request.path }}?{{ request.GET.urlencode }}&delete=1">当前网址加参数 delete</a>

比如我们可以判断 delete 参数是不是 1 来删除当前的页面内容。


完整的内容参考官方文档：<https://docs.djangoproject.com/en/1.9/ref/templates/builtins/>
