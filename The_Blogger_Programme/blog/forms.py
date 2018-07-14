from django import forms
from django.forms import ModelForm
from .models import Blog

class BlogForm(forms.Form):
    blog_url = forms.URLField(label='Blog url', max_length=200)

    class Meta:
        model = Blog
        fields = ('blog_url',)

    def saved(self):
        data = self.cleaned_data
        return data['blog_url']
