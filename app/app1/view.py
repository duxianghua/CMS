from django.shortcuts import render
from .models import Host

def host_info(request):
	host_list = Host.objects.all()
	context = {'host_list':host_list}
	return render(request,'host_info.html',context)

def index1(request,url):
	host_list = Host.objects.all()
	context = {'host_list':host_list}
	return render(request, url,context)
