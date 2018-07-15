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
    try:
        context = ""
        form = BlogForm()
        if request.method=='POST':
            form = BlogForm(request.POST)
            print(form)
            if form.is_valid():
                new_blog = Blog(blog_url=request.POST['blog_url'])
                new_blog.save()
                return redirect('home')
            else:
                comment = "Wrong URL."
        else:
            form = BlogForm()
            comment = ""
        context = {
    		'form': form,
            'comment': comment,
            }
    except:
        context = {
            'comment': "URL already exists.",
        }
    return render(request, '../templates/add_blog.html', context)


def delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('admin_view')


def update(id, upa, pda):
    blog = Blog.objects.get(id=id)
    if upa != None and pda != None:
        blog.upa = upa['upa']
        blog.pda = pda['pda']
        blog.save()
    return blog


def api_moz(blog):
    try:
        accesID = "mozscape-b483995429"
        secretKey = "ea99d45073c90c59ac64d7fbbfd9a9bb"
        upa = "https://lsapi.seomoz.com/linkscape/url-metrics/" + blog.blog_url + "?Cols=34359738368"
        pda = "https://lsapi.seomoz.com/linkscape/url-metrics/" + blog.blog_url + "?Cols=68719476736"
        response_upa = requests.get(upa, auth=(accesID, secretKey))
        response_pda = requests.get(pda, auth=(accesID, secretKey))
        upa_content = response_upa.json()
        pda_content = response_pda.json()
        blog = update(blog.id, upa_content, pda_content)
    except:
        print("Exception.")
    return blog


def admin_view(request):
    blog_list = Blog.objects.order_by('id')
    for blog in blog_list:
        if blog.upa == None or blog.pda == None:
            blog = api_moz(blog)
            blog_list = Blog.objects.order_by('id')
    context = {
        'blog_list': blog_list,
        'number_of_results': len(blog_list),
    }
    return render(request, "../templates/admin.html", context)
