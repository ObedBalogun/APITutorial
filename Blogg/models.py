from django.db import models

class BlogPost(models.Model):
    Name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    Content = models.TextField(default='')
    Title = models.CharField(max_length=250, default='None')

    def __str__(self):
        return self.Name