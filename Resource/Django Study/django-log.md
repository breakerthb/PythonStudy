# Django日志系统

django中日志和国际化都是采用彼Python的标准库来实现的，其中国际化是使用的GNU的gettext模块，日志采用的是logging模块。

# 创建log目录

在project目录下创建log目录，用来保存日志文件。

# 配置

日志配置包括四个部分：记录器，处理器，过滤器和格式器，下面我们来一一讲解

## 1. 记录器

一个记录器是日志系统的一个实体，每一个记录器是一个已经命名好的可以将消息为进程写入的“桶”。

每一个记录器都会有一个日志等级，每个等级描述了记录器即将处理的信息的严重性，python定义了以下五个等级：

	debug：出于调试目的的低层次系统信息
	info：普通的系统信息
	warning：描述已经发生的小问题
	error：描述已经发生的主要问题
	critical：描述已经发生的严重问题

每一条被写入记录器的信息成为一条日志记录，每条日志记录都有一个表明该记录严重性的日志等级，每条日志信息也会包含一些有用的元信息表明已经被记录的事件，比如栈追溯和错误代码。

当一条信息被发往记录器的时候，消息的记录等级会和记录器的等级相比较，如果符合甚至超越当前等级，则被发往处理器处理，否则会被忽略掉。

## 2. 处理器

处理器是决定日志记录器中对应的实体消息发生了什么的引擎，描述了一个具体的日志行为，比如输出到屏幕，或者一个文件，抑或一个网络socket。

和记录器一样，没有到达相应等级的消息会被忽略。

一个记录器可以有多个处理器，一个处理器可以有不同的日志等级，因此你可以根据消息的重要性而提供不同的提示。

## 3. 过滤器

过滤器是用来提供额外的控制，控制哪些日志记录可以被传给处理器处理。

默认情况下，只要日志消息符合相应的等级要求就会传给对应的处理器处理，然而，通过安装过滤器，你可以在日志记录过程中设置额外的内容，例如，你可以安装一个过滤器使得某个源只有error级别的消息才会被发送。你也可以使用过滤器修改之前会被发送的消息，例如，你可以写一个过滤器使得符合某些条件的error等级的消息降级为warning等级。

过滤器可以给处理器和记录器使用，多个过滤器可以级联使用。

## 4. 格式器

控制日志输出的格式，格式使用python的字符串控制格式

打开setting.py，加入下面代码：

	DEBUG = True
	
	LOGGING = {
	    'version': 1,
	    'disable_existing_loggers': False,
	    'filters': { #过滤器
	        'require_debug_true': {
	            '()': 'django.utils.log.RequireDebugTrue',
	        }, # 针对 DEBUG = True 的情况
	    },
	    'formatters': { #格式器
	        'standard': {
	            'format': '%(levelname)s %(asctime)s %(pathname)s %(filename)s %(module)s %(funcName)s %(lineno)d: %(message)s'
	        }, 
		# 对日志信息进行格式化，每个字段对应了日志格式中的一个字段，更多字段参考官网文档，我认为这些字段比较合适，输出类似于下面的内容
	       # INFO 2016-09-03 16:25:20,067 /home/ubuntu/mysite/views.py views.py views get 29: some info...
	    },
	    'handlers': {#处理器，在这里定义了三个处理器
	        'mail_admins': {
	            'level': 'ERROR',
	            'class': 'django.utils.log.AdminEmailHandler',
	             'formatter':'standard'
	        },
	        'file_handler': {
	             'level': 'DEBUG',
	             'class': 'logging.handlers.TimedRotatingFileHandler',
	             'filename': 'log/abc.log', # 自定义log文件位置
	             'formatter':'standard'
	        }, # 用于文件输出
	        'console':{
	            'level': 'INFO',
	            'filters': ['require_debug_true'],
	            'class': 'logging.StreamHandler',
	            'formatter': 'standard'
	        },
	    },
	    'loggers': { #定义了三个记录器
	        'django': {
	            'handlers' :['file_handler', 'console'],
	            'level':'DEBUG',
	            'propagate': True # 是否继承父类的log信息
	        }, # handlers 来自于上面的 handlers 定义的内容
	        'django.request': {
	            'handlers': ['mail_admins'],
	            'level': 'ERROR',
	            'propagate': False,
	        },
	    }
	}

注意，自定义log文件位置需要指定在新创建的目录中。

# 使用

	import logging
	logger = logging.getLogger("django") # 为loggers中定义的名称
	logger.info("some info...")

一共有5种可用方法。

ref: <http://doc.okbase.net/qwj-sysu/archive/123835.html>