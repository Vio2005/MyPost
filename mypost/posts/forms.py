from django import forms
from .models import *

class PostCreateForm(forms.Form):
    title=forms.CharField()
    body=forms.CharField()
    photo=forms.ImageField()

class PostModelForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','photo','post_body']