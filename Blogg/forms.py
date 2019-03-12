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
class EntryForm(forms.Form):
    # visitor_name=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Visitor Name'}), label="")
    Name= forms.CharField(max_length=500, required=True,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholer':'Your Name'}),label="")
    Content=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Post Here'}), label="")
