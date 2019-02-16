from .views import BlogPostCreateView,BlogPostRUDView
from django.conf.urls import url

app_name = 'Blogg'

urlpatterns = [
    url(r'^$',BlogPostCreateView.as_view()),
    url(r'(?P<pk>\d+)/',BlogPostRUDView.as_view())
]