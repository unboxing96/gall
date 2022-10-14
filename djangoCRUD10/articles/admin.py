from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "user_name", "created_at")


admin.site.register(Article)
