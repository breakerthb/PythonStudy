from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from myapp.models import Message

def index(request):
    mlist = Message.objects.all()
    return render(request, 'home.html', {'mlist' : mlist})
    
def add(request):
    _name = request.GET['name']
    _content = request.GET['content']
    
    m = Message(name=_name, content=_content)
    m.save()
    
    return HttpResponseRedirect('/')
    
def delete(request):
    _id = request.GET['id']
    
    Message.objects.filter(id=_id).delete()
    
    return HttpResponseRedirect('/')