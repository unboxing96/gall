from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 90},
    )
