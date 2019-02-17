from django.urls import path
from .views import create_post, update_post, delete_post,index

urlpatterns=[
    path('',index, name= 'homepage'),
    path('',create_post, name= 'create_post'),
]