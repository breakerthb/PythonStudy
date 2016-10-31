# Django静态文件管理

# 参考：

- 1.8版本之前：<http://www.ziqiangxuetang.com/django/django-static-files.html>
- 1.8.2版本：<http://python.usyiyi.cn/documents/django_182/howto/static-files/index.html>

静态文件是指:

- js, css文件
- 图片，视频等文件

*注意：*

静态文件在Debug阶段和部署阶段使用方法有些出入。我们这里主要讨论DEBUG=True时的使用方法。

# 配置静态文件

## 1. django.contrib.staticfiles

Django提供[django.contrib.staticfiles](http://python.usyiyi.cn/documents/django_182/ref/contrib/staticfiles.html#module-django.contrib.staticfiles)来帮助管理静态文件。首先确认django.contrib.staticfiles 包含在你的INSTALLED_APPS 中。

![](http://i.imgur.com/beRE6xk.png)

## 2. 定义STATIC_URL变量

在settings 文件中定义STATIC_URL，例如：

    STATIC_URL = '/static/'

## 3. 模板中引用

在模板中，你可以硬编码/static/my_app/myexample.jpg 这样的URL，或者使用static 模板标签以及配置的STATICFILES_STORAGE为给出的相对路径创建URL（这使得换成CDN 来保存静态文件更加容易）。

	{% load staticfiles %}
	<img src="{% static "image/image1.png" %}" alt="My image"/>
	<img src="/static/image/image1.png" alt="My image"/>

这里使用动态路径和硬路径都可以达到效果。

在你的应用中，将静态文件存储在名为static 目录下。例如：

	.
	├── db.sqlite3
	├── manage.py
	├── my_site
	│   ├── __init__.py
	│   ├── __init__.pyc
	│   ├── settings.py
	│   ├── settings.pyc
	│   ├── urls.py
	│   ├── urls.pyc
	│   ├── wsgi.py
	│   └── wsgi.pyc
	├── showImg1
	│   ├── __init__.py
	│   ├── __init__.pyc
	│   ├── admin.py
	│   ├── admin.pyc
	│   ├── migrations
	│   │   ├── __init__.py
	│   │   └── __init__.pyc
	│   ├── models.py
	│   ├── models.pyc
	│   ├── static
	│   │   └── image
	│   │       └── image1.png
	│   ├── templates
	│   │   └── index.html
	│   ├── tests.py
	│   ├── views.py
	│   └── views.pyc
	└── showImg2
	    ├── __init__.py
	    ├── __init__.pyc
	    ├── admin.py
	    ├── admin.pyc
	    ├── migrations
	    │   ├── __init__.py
	    │   └── __init__.pyc
	    ├── models.py
	    ├── models.pyc
	    ├── static
	    │   └── image
	    │       └── image2.png
	    ├── tests.py
	    └── views.py

运行站点，查看效果。显示了两张图片。修改html页面如下：

	{% load staticfiles %}
	<img src="{% static "image/image1.png" %}" alt="My image"/>
	<img src="{% static "image/image2.png" %}" alt="My image"/>

这次我们引用了两个app钟的static目录，两张图片也能正常显示。

*这说明：* django.contrib.staticfiles寻找/static/路径时会默认在每个app的根目录中寻找。

## 4. 启用静态文件服务

在开发过程中，如果你使用django.contrib.staticfiles，当DEBUG 设置成True 时，runserver 会自动启用静态文件服务（参见[django.contrib.staticfiles.views.serve()](http://python.usyiyi.cn/documents/django_182/ref/contrib/staticfiles.html#django.contrib.staticfiles.views.serve)）。

*这个方法非常低效而且可能不安全，所以它不适合线上环境。*

关于线上环境保存静态文件的策略，参见部[部署静态文件](http://python.usyiyi.cn/documents/django_182/howto/static-files/deployment.html)。

你的项目可能还有一些静态文件不属于任何一个应用。那样我们需要在settings 文件中定义一个目录列表（STATICFILES_DIRS），Django 会在其中查找静态文件。
	
	STATICFILES_DIRS = (
	    os.path.join(BASE_DIR, "static"),
	    #os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/'),
	    #'/var/www/static/',
	)

我们在my_site跟部门下创建static目录，此时这个新建目录会被加入到寻找静态文件的列表中。

# 静态文件的命名空间

现在，我们虽然能够将静态文件直接放在my_app/static/之下（而不用创建另外一个my_app 子目录），但是这是一个坏主意。Django 将使用它找到的名称匹配第一个静态文件， 如果你在另外一个不同 的应用中有相同名称的静态文件，Django 将无法区分它们。我们需要让Django 能够找到正确的静态文件，最简单的方法是给它们加上命名空间。方法是将这些静态文件放在与应用同名的另外一个目录中。


# 手动启动静态文件服务

如果django.contrib.staticfiles 不在INSTALLED_APPS 中，你仍然可以使用django.contrib.staticfiles.views.serve() 视图手工启用静态文件服务。

例如，如果STATIC_URL 定义为/static/，你可以通过在urls.py 中加入以下代码片段启用：

	from django.conf import settings
	from django.conf.urls.static import static
	
	urlpatterns = [
	    # ... the rest of your URLconf goes here ...
	] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 引用其他静态文件

## 1. CSS文件

    <head>
        <title>Welcome</title>
        {% load staticfiles %}
        <link rel=stylesheet type="text/css" href="{% static "default.css" %}" title="cool">
    </head>

## 2. JS文件

# 部署

django.contrib.staticfiles 提供一个便捷的管理命令用于将静态文件收集到一个目录中,这样你就可以轻松地供给这些文件

## 1. 将 STATIC_ROOT设置为你提供文件的目录,例子如下

    STATIC_ROOT = "/var/www/example.com/static/"

## 2. 运行collectstatic管理命令

    $ python manage.py collectstatic

这会将所有你在所有static目录下的所有的文件都复制到 STATIC_ROOT 目录中

## 3. 使用你所选择的Web服务器来提供这些文件Deploying static files 讲了一些常见的讲台文件部署策略


具体可以参考：<http://python.usyiyi.cn/documents/django_182/ref/contrib/staticfiles.html#module-django.contrib.staticfiles>