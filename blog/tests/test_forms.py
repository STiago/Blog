from django.test import TestCase
from blog.models import Blog
from django.core.urlresolvers import reverse
from blog.forms import BlogForm

class BlogFormTest(TestCase):
    def test_valid_blog_form(self):
        blog_url = "www.travelblog.org"
        b = Blog.objects.create(blog_url = blog_url)
        data = {'blog_url': b.blog_url,}
        form = BlogForm(data=data)
        self.assertTrue(form.is_valid())
