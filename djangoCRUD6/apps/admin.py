from django.contrib import admin
from .models import App

# Register your models here.


class AppAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")


admin.site.register(App, AppAdmin)
