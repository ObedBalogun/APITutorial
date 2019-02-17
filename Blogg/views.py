from django.shortcuts import render
from .models import BlogPost
from .forms import PostForm

def index(request):
    posts = BlogPost.objects.all()
    render(request,'index.html',{'posts':posts})

def create_post(request):
    form = PostForm(request.POST or None)
    render(request,'create_post.html',{'form':form})

def delete_post(request):
    pass

def update_post(request):
    pass
