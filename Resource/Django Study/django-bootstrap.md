# bootstrap

# 文件介绍

## bootstrap.css

是完整的bootstrap样式表，未经压缩过的，可供开发的时候进行调试用

## bootstrap.min.css

是经过压缩后的bootstrap样式表，内容和bootstrap.css完全一样，但是把中间不必要的空格之类的东西都删掉了，所以文件大小会比bootstrap.css小，可以在部署网站的时候引用，如果引用了这个文件，就没必要引用bootstrap.css了

## bootstrap-responsive.css

这个是在对bootstrap框架应用了响应式布局之后所需要的CSS样式表，如果你的网站项目不准备做响应式设计，就不需要引用这个CSS。

## bootstrap-responsive.min.css

和bootstrap.min.css的作用是一样的，是bootstrap-responsive.css的压缩版

##　bootstrap.js

这个是bootstrap的灵魂所在，是bootstrap的所有js指令的集合，你看到bootstrap里面所有的js效果，都是由这个文件控制的，这个文件也是一个未经压缩的版本，供开发的时候进行调试用

## bootstrap.min.js 

是bootstrap.js的压缩版，内容和bootstrap.js一样的，但是文件大小会小很多，在部署网站的时候就可以不引用bootstrap.js，而换成引用这个文件了

# 常用文件下载

	<!-- 新 Bootstrap 核心 CSS 文件 -->
	<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css">
	
	<!-- 可选的Bootstrap主题文件（一般不用引入） -->
	<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap-theme.min.css">
	
	<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
	<script src="http://cdn.bootcss.com/jquery/1.11.1/jquery.min.js"></script>
	
	<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
	<script src="http://cdn.bootcss.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>

ref: <http://v3.bootcss.com/getting-started/>