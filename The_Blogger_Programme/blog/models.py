from django.db import models

class Blog(models.Model):
 	blog_url = models.URLField(max_length=200)
