from django.db import models
from django.forms import CharField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
