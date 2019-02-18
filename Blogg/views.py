from django.shortcuts import render,redirect
from .models import BlogPost
from .forms import PostForm

def index(request):
    posts = BlogPost.objects.all()
    return render(request,'Blogg/index.html',{'posts':posts})

def create_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        redirect('index')
    return render(request,'create_post.html',{'form':form})

def delete_post(request, post_id):
    posts = BlogPost.objects.get(pk=post_id)
    posts.delete()
    return redirect('index')

def update_post(request):
    pass
