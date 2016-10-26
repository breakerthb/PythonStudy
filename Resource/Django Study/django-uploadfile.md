# Django文件上传

# 创建目录

在project根目录创建一个新文件夹"uploads"，之后在settings.py中配置路径：

	#配置文件的上传路径
	MEDIA_URL = 'uploads/' # 相对路径
	MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads') #绝对路径

目录的使用请参考：[Django常用目录](https://github.com/breakerthb/PythonStudy/blob/master/Resource/Django%20Study/django-folders.md)

# 模板文件(html)

    <form method="POST" action="/upload/" enctype="multipart/form-data">
        <!--
        <input type="text" name="byd" id="byd" placeholder="请输入字符串">
        -->
        <input type="file" name="file" value="手动点击上传图片"><br/>
        <input type="submit" name="提交">
    </form>
 
# 使用基础表单功能上传

在views.py中添加下面代码：

	import os
	import json
	from django.conf import settings
	
	stat = {'status':False,'data':None,'msg':None}
	def upload_file(request):
	    if request.method == 'POST':
	        try:
	            #user = request.POST.get('byd')
	            img = request.FILES.get('file')
	            img_path = os.path.join(settings.MEDIA_URL, img.name)
	            
	            f = open(img_path,'wb')
	            for chunk in img.chunks():
	                f.write(chunk)
	            f.close()
	                
	            stat['status'] = True
	            stat['data'] = img_path
	        except Exception as e:
	            stat['msg'] = str(e)
	        finally:
	            return HttpResponse(json.dumps(stat))
	    else:
	        return render(request,'upload.html')

启动服务，首先看到下面页面：

![](http://i.imgur.com/PuzXVCO.png)

选择本地文件后点击“提交查询”，显示下面内容：

![](http://i.imgur.com/JfykrDT.png)

上传成功。在uploads目录下可以看到上传的文件。

如果上传失败，会显示报错的json信息。

## CSRF错误

上传中，可能出现下面的错误。

![](http://i.imgur.com/m2hxfTA.png)

我们又两种解决方法：

### 方法一：

在settings.py中，注掉一行代码：

	MIDDLEWARE_CLASSES = [
	    'django.middleware.security.SecurityMiddleware',
	    'django.contrib.sessions.middleware.SessionMiddleware',
	    'django.middleware.common.CommonMiddleware',
	    #'django.middleware.csrf.CsrfViewMiddleware',
	    'django.contrib.auth.middleware.AuthenticationMiddleware',
	    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	    'django.contrib.messages.middleware.MessageMiddleware',
	    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	]

### 方法二：

在模板文件的form中添加下面代码：

	<form>
	    {% csrf_token %}
	</form>

修改view.py代码：

	return render(request,'upload.html')

改为：

	return render(request,'upload.html', context_instance=RequestContext(request))

推荐使用第二种方法。	

*注意*：

- 表单上传的文件对象存储在类字典对象request.FILES中
- 表单格式需为multipart/form-data
- request.FILES中的键来自于表单中的\<input type="file" name="" />的name值
- request.FILES中的值均为UploadedFile类文件对象
- 注意上传的是二进制文件，所以需使用wb模式打开文件

## UploadedFile

UploadedFile是类文件对象，具有以下方法和属性：

- UploadedFile.read()

读取整个上传文件的数据，文件较大时慎用。

- UploadedFile.multiple_chunks(chunk_size=None)

判断文件是否足够大，一般为2.5M

- UploadedFile.chunks(chunk_size=None)

返回一个生成器对象，当multiple_chunks()为True时应该使用这个方法来代替read().

- UploadedFile.name

上传文件的name。

- UploadedFile.size

上传文件的大小。

- UploadedFile.content_type

上传文件时的content_type报头，例如(e.g. text/plain or application/pdf). 

- UpladedFile.charset


# 用django自带的form类上传

新建文件form.py

	from django import forms
	
	class UploadFileForm(forms.Form):
	    #title = forms.CharField(max_length=50)
	    file = forms.FileField()

处理这个form的视图收到了在request.FILES中的文件数据。从上述form来的数据可以通过request.FILES['file']来存取。

*注意*：只有当request方法是POST，且发送request的<form>有属性enctype="multipart/form-data"时，request.FILES中包含文件数据，否则request.FILES为空。

以下视图函数：

	stat = {'status':False,'data':None,'msg':None}
	def upload_file(request):
	  if request.method == 'POST':
	     form = UploadFileForm(request.POST, request.FILES)
	     if form.is_valid():
	        handle_uploaded_file(request.FILES['file'])
	        return HttpResponse(json.dumps(stat))
	  else:
	     form = UploadFileForm()
	  return render(request, 'upload.html', {'form': form}, context_instance=RequestContext(request))
	
	def handle_uploaded_file(f):
	    img_path = os.path.join(settings.MEDIA_URL, f.name)
	    destination = open(img_path, 'wb+')
	    for chunk in f.chunks():
	        destination.write(chunk)
	    destination.close()

必须要将request.FILES传给form的构造函数，才能将文件数据绑定到form.

相应的，模板文件也可以做下面的修改：

	<form method="POST" action="/upload/" enctype="multipart/form-data">
         {% csrf_token %}
         {{ form }}
        <br/>
        <input type="submit" name="提交">
    </form>

当然，html不做修改也可以使用。

 
# Ajax实现文件上传

ref:<http://www.cnblogs.com/pycode/p/upload.html>