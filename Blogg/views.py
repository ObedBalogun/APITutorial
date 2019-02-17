from django.shortcuts import render
from .models import BlogPost


def index(request):
    posts = BlogPost.objects.all()
    render(request,'index.html',{'posts':posts})