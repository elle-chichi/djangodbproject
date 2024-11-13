from django.shortcuts import render,get_object_or_404
from django.template.context_processors import request

from .models import Blogpost
# Create your views here.

def blog_list(request):
    posts=Blogpost.objects.all()
    return render(request,'blog_list.html',{'posts':posts})

def blog_detail(request,id):
    post=get_object_or_404(Blogpost,id=id)
    return render(request,'blog_details.html',{'post':post})


