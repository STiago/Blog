from django.shortcuts import render, redirect
from . import models
from .forms import BlogForm
from .models import Blog
import requests
import psycopg2

response = requests.get("https://moz.com/products/mozscape/access")
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
    if request.method=='POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            instance = Blog(blog_url=request.POST['blog_url'])
            instance.save()
            return redirect('home')
    else:
        form = BlogForm()
    context = {
		'form': form,
        }
    return render(request, '../templates/add_blog.html', context)


def delete(request,id):
    instance = Blog.objects.get(id=id)
    instance.delete()
    return redirect('home')


def update(id, upa, pda):
    instance = Blog.objects.get(id=id)
    print(upa)
    if upa != None and pda != None:
        instance.upa = upa['upa']
        instance.pda = pda['pda']
        instance.save()


def api_moz(request):
    blog_list = Blog.objects.order_by('id')
    for blog in blog_list:
        accesID = "mozscape-b483995429"
        secretKey = "ea99d45073c90c59ac64d7fbbfd9a9bb"
        upa = "https://lsapi.seomoz.com/linkscape/url-metrics/" + blog.blog_url + "?Cols=34359738368"
        pda = "https://lsapi.seomoz.com/linkscape/url-metrics/" + blog.blog_url + "?Cols=68719476736"
        response_upa = requests.get(upa, auth=(accesID, secretKey))
        response_pda = requests.get(pda, auth=(accesID, secretKey))
        upa_content = response_upa.json()
        pda_content = response_pda.json()
        update(blog.id, upa_content, pda_content)


def admin_view(request):
    print(api_moz(request))
    blog_list = Blog.objects.order_by('id')
    context = {
        'blog_list': blog_list,
        'number_of_results': len(blog_list),
    }
    return render(request, "../templates/admin.html", context)
