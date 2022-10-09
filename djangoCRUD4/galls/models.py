from django.db import models

# Create your models here.
class Gall(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user_id = models.CharField(max_length=15)
    user_pw = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
