from django.urls import path
from .views import create_post, update_post, delete_post,index
app_name = 'Blogg'


urlpatterns=[
    path('',index, name= 'homepage'),
    path('',create_post, name='create_post'),
    path('delete_post/<int:post_id>',delete_post, name='delete_post'),
]