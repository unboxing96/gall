from django.urls import path
from . import views

app_name = "galls"

urlpatterns = [
    path("", views.index, name="index"),
]
