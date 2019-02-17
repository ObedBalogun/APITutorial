from .models import BlogPost
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields =(
            'Name',
            'Title',
            'Content',
        )