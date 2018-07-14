from django.shortcuts import render, redirect
from . import models
from .forms import BlogForm
from .models import Blog
import requests
import psycopg2

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)

def home(request):
    blog_list = Blog.objects.order_by('id')
    context = {
        'blog_list': blog_list,
        'number_of_results': len(blog_list),
    }
    return render(request, "../templates/home.html", context)


def add_blog_url(request):
    form = BlogForm()
    print(form)
    if request.method=='POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_url =request.POST['blog_url']
            instance = Blog(blog_url=request.POST['blog_url'])
            #instance.save()
            return redirect('home')
    else:
        form = BlogForm()
    context = {
		'form': form,
        }
    return render(request, '../templates/add_blog.html', context)
