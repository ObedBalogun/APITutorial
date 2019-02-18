from rest_framework import serializers
from Blogg.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = (
            'pk',
            'Name',
            'date_created',
            'Title',
            'Content'
        )
    read_only_fields =['date_created','pk']
