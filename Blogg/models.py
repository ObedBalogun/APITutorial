from django.db import models

class BlogPost(models.Model):
    name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=250)

    def __str__(self):
        return self.name