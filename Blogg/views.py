from django.shortcuts import render,redirect
from .models import BlogPost
from .forms import PostForm
import urllib.request as url


def homepage(request):
    posts = BlogPost.objects.all()
    # url_link = url.Request('http://pythonprogramming.net')
    # link = url.urlopen(url_link)
    # link_data = link.read()
    return render(request,'Blogg/index.html',{'posts':posts})


def create_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        redirect('Blogg:homepage')
    return render(request,'Blogg/create_post.html',{'form':form})

def delete_post(request, post_id):
    posts = BlogPost.objects.get(pk=post_id)
    if request.method == 'POST':
        posts.delete()
        return redirect('Blogg:homepage')

def update_post(request, post_id):
    posts = BlogPost.objects.get(pk=post_id)
    form = PostForm(request.POST or None, instance=posts)
    if form.is_valid():
        form.save()
    return render(request,'Blogg/index.html',{'posts':posts,
                                              'form':form})
