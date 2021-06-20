from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="blog_index"),
    path("login/", views.LogIn.as_view(), name="login"),
    path("logout/", views.LogOut.as_view(), name="logout"),
]


