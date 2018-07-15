from django.db import models

class Blog(models.Model):
    blog_url = models.URLField(max_length=200, unique=True)
    upa = models.IntegerField(null=True)
    pda = models.IntegerField(null=True)
