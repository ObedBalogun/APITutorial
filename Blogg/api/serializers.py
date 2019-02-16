from rest_framework import serializers
from Blogg.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = (
            'pk',
            'name',
            'date_created',
            'content'
        )

