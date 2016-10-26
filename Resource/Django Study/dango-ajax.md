# Django Ajax

# get方式

这里用<https://www.zybuluo.com/breakerthb/note/405631>中的get例子。我们改写成利用jquery实现部分刷新提交。

修改 index.html 文件

	<!DOCTYPE html>
	<html>
	<body>
	<p>请输入两个数字</p>
	<form action="/add/" method="get">
	    a: <input type="text" id="a" name="a"> <br>
	    b: <input type="text" id="b" name="b"> <br>
	    <p>result: 
	    <span id='result'></span>
	    </p>
	    <button type="button" id='sum'>提交</button>
	</form>
	 
	{% load staticfiles %}
	<script src="{% static "jquery.min.js" %}"></script>
	<!-- 
	<script src="http://apps.bdimg.com/libs/jquery/1.11.1/jquery.min.js"></script>
	-->
	<script>
	    $(document).ready(function(){
	      $("#sum").click(function(){
	        var a = $("#a").val();
	        var b = $("#b").val();
	 
	        $.get("/add/",{'a':a,'b':b}, function(ret){
	            $('#result').html(ret)
	        })
	      });
	    });
	</script>
	</body>
	</html>


在原来的基础上，在一些元素上加了 id, 以便于获取值和绑定数据，然后我们用了jQuery.get() 方法，并用 $(selector).html() 方法将结果显示在页面上，如下图：

![http://www.ziqiangxuetang.com/media/uploads/images/QQ20141020-1\_20141020\_123355\_96.png](http://www.ziqiangxuetang.com/media/uploads/images/QQ20141020-1_20141020_123355_96.png)


## 关于请求头和 request.is_ajax() 方法使用

views.py 中可以用  request.is_ajax() 方法判断是否是 ajax 请求，需要添加一个 HTTP 请求头：

- 原生javascript：

		xmlhttp.setRequestHeader("X-Requested-With", "XMLHttpRequest");

- jQuery：

		用 $.ajax 方法代替 $.get，因为 $.get 在 IE 中不会发送 ajax header

服务器端会将请求头的值全部大写，中划线改成下划线，并在非标准的头前面加上 HTTP_，这个过程可以认为相当于以下Python代码：

	STANDARD_HEADERS = ['REFER', 'HOST', ...] # just for example
	 
	def handle_header(value):
	    value = value.replace('-', '_').upper()
	 
	    if value in STANDARD_HEADERS:
	        return value
	 
	    return 'HTTP_' + value

对之前代码做如下修改：

- html

		<html>
		<meta charset="utf-8">
		
		<head>
		<script>
		function ajax_request()
		{
		    var xmlhttp;
		    if (window.XMLHttpRequest) {
		        // code for IE7+, Firefox, Chrome, Opera, Safari
		        xmlhttp=new XMLHttpRequest();
		      } else {
		        // code for IE6, IE5
		        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		}
		
		xmlhttp.onreadystatechange=function() {
		  if (xmlhttp.readyState==4 && xmlhttp.status==200) {
		      document.getElementById("result").innerHTML=xmlhttp.responseText;
		  }
		}
		
		var a = document.getElementById("a").value;
		var b = document.getElementById("b").value;
		xmlhttp.open("GET", "/add/" + a + "/" + b + "/", true);
		xmlhttp.setRequestHeader("X-Requested-With", "XMLHttpRequest");
		xmlhttp.send();
		// ajax 教程：http://www.ziqiangxuetang.com/ajax/ajax-tutorial.html
		}
		</script>
		
		</head><body>
		<div id="myDiv"><h2>输入两个数求和</h2></div>
		a: <input id="a"><br>
		b: <input id="b"><br>
		<button type="button" onclick="ajax_request()">求和</button>
		<div>结果：<span id="result"></span></div>
		</body>
		</html>

- url.py

		url(r'^add/((?:-|\d)+)/((?:-|\d)+)/$', getpage_views.add, name='add'),

- views.py

		def add(request, a, b):
		    if request.is_ajax():
		        ajax_string = 'ajax request: '
		    else:
		        ajax_string = 'not ajax request: '
		    c = int(a) + int(b)
		    return HttpResponse(ajax_string + str(c))

测试一下，首先在页面中利用Ajax提交，结果如下：

![](http://i.imgur.com/vWGyMaA.png)

再用url直接访问get方法：

![](http://i.imgur.com/xpGObxo.png)


# 传递复杂结构

更复杂的例子，传递一个数组或字典到网页，由JS处理，再显示出来。


ref:<http://www.ziqiangxuetang.com/django/django-ajax.html>