# Django文件上传

# html(模板文件):

	<form enctype="multipart/form-data" method="POST" action="upload/"> 
	   <input type="file" name="file" />
	   <br /> 
	   <input type="submit" value="上传文件" /> 
	</form>
 
新建文件form.py

	from django import forms
	
	class UploadFileForm(forms.Form):
	    title = forms.CharField(max_length=50)
	    file = forms.FileField()

处理这个form的视图收到了在request.FILES中的文件数据。从上述form来的数据可以通过request.FILES['file']来存取。

*注意*：只有当request方法是POST，且发送request的<form>有属性enctype="multipart/form-data"时，request.FILES中包含文件数据，否则request.FILES为空。

以下视图函数：

	from django.http import HttpResponseRedirect
	from django.shortcuts import render_to_response
	from somewhere import handle_uploader_file
	
	def upload_file(request):
	  if request.method == 'POST':
	     form = UploadFileForm(request.POST, request.FILES)
	     if form.is_valid():
	        handle_uploaded_file(request.FILES['file'])
	        return HttpResponseRedirect('/success/url')
	  else:
	     form = UploadFileForm()
	  return render_to_response('upload.html', {'form': form})

必须要将request.FILES传给form的构造函数，才能将文件数据绑定到form.

处理上传文件
字典request.FILES中的每一个条目都是一个UploadFile对象。UploadFile对象有如下方法：
1、UploadFile.read():
从文件中读取全部上传数据。当上传文件过大时，可能会耗尽内存，慎用。
2、UploadFile.multiple_chunks():
如上传文件足够大，要分成多个部分读入时，返回True.默认情况,当上传文件大于2.5M时，返回True。但这一个值可以配置。
3、UploadFile.chunks():
返回一个上传文件的分块生成器。如multiple_chunks()返回True,必须在循环中使用chrunks()来代替read()。一般情况下直接使用chunks()就行。
4、UploadFile.name():上传文件的文件名
5、UplaodFile.size():上传文件的文件大小（字节）
由上面的说明可以写出handle_uploaded_file函数

	def handle_uploaded_file(f):
	    destination = open('some/file/name.txt', 'wb+')
	    for chunk in f.chunks():
	        destination.write(chunk)
	    destination.close()

详细点：

	def handle_uploaded_file(f):
	    file_name = ""
	
	    try:
	        path = "media/editor" + time.strftime('/%Y/%m/%d/%H/%M/%S/')
	        if not os.path.exists(path):
	            os.makedirs(path)
	            file_name = path + f.name
	            destination = open(file_name, 'wb+')
	            for chunk in f.chunks():
	                destination.write(chunk)
	            destination.close()
	    except Exception, e:
	        print e
	
	    return file_name


 

# 上传文件保存的位置

保存上传文件前，数据需要存放在某个位置。默认时，当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。意味着保存文件只有一次从内存读取，一次写磁盘。
但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。

改变upload handler的行为
三个设置控制django文件上传的行为：
FILE_UPLOAD_MAX_MEMORY_SIZE:直接读入内存的最大上传文件大小（字节数）。当大于此值时，文件存放到磁盘。默认2.5M字节
FILE_UPLOAD_TEMP_DIR
FILE_UPLOAD_PERMISSIONS:权限
FILE_UPLOAD_HANDLERS
上传文件真正的处理器。修改此项设置可以完成自定义django上传文件的过程。
默认是：

("django.core.files.uploadhandler.MemoryFileUploadHandler",
"django.core.files.uploadhandler.TemporaryFileUploadHandler",)

先尝试装入内存，如不行就存入到临时文件。

上传文件封装方法：
复制代码

	'''文件上传'''
	def handle_uploaded_file(f):
	    file_name = ""
	
	    try:
	        path = "media/image" + time.strftime('/%Y/%m/%d/%H/%M/%S/')
	        if not os.path.exists(path):
	            os.makedirs(path)
	            file_name = path + f.name
	            destination = open(file_name, 'wb+')
	            for chunk in f.chunks():
	                destination.write(chunk)
	            destination.close()
	    except Exception, e:
	        print e
	
	    return file_name

复制代码

 



2、表单中得包含{% csrf_token %}标签

<form>
    {% csrf_token %}
</form>

3、在 view 中, 使用 django.template.RequestContext 而不是 Context。render_to_response, 默认使用 Context.。需要改成 RequestContext。

#额外需要导入的模块
from django.template import RequestContext

#视图函数中给render_to_response增加一个参数:context_instance=RequestContext(request)

return render_to_response('template.html',
          传递给模板的字典,
          context_instance=RequestContext(request)
    )

#比如这样
def confset(request):
    avg = {'privatetitle': '配置管理|配置下发', 'STATIC_URL': '/static'}
    return render_to_response('confapp/confset.html', avg, context_instance=RequestContext(request))