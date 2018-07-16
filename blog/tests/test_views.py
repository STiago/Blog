from django.test import TestCase
from blog.models import Blog
from django.core.urlresolvers import reverse
from blog.views import *

class BlogViewTest(TestCase):
    def setUp(self):
        blog_url = "www.travelblog.org"
        Blog.objects.create(blog_url = blog_url)

    def tearDown(self):
        pass

    def test_blog_has_upa(self):
        """Blosg that have an UPA are correctly identified"""
        blog = Blog.objects.get(blog_url="www.travelblog.org")
        result = api_moz(blog)
        self.assertEqual(result.upa, 61)

    def test_blog_has_pda(self):
        """Blosg that have an PDA are correctly identified"""
        blog = Blog.objects.get(blog_url="www.travelblog.org")
        result = api_moz(blog)
        self.assertEqual(result.pda, 76)

    def test_view_url_exists_at_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_is_accessible_by_name(self):
        resp = self.client.get(reverse('admin_view'))
        self.assertEqual(resp.status_code, 200)
