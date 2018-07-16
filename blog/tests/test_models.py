from django.test import TestCase
from blog.models import Blog
from django.core.urlresolvers import reverse
from blog.forms import BlogForm


class BlogModelTest(TestCase):
    blog_url = "www.travelblog.org"
    def create_blog(self, blog_url):
        return Blog.objects.create(blog_url=blog_url)

    def test_blog_creation(self):
        blog_url="www.travelblog.org"
        w = self.create_blog(blog_url)
        self.assertTrue(isinstance(w, Blog))
        self.assertEqual(w.blog_url , "www.travelblog.org")
