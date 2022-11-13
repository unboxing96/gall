from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
    path("password_change/", views.password_change, name="password_change"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
]
