from django.views.generic import TemplateView, RedirectView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class HomePage(TemplateView):
    template_name = "blog/index.html"


class LogIn(TemplateView):
    """Login View"""
    template_name = "login.html"

    def post(self, request):
        """get request data for the login"""
        print(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        email = email.strip()
        password = password.strip()
        # authenticate user in the Databse
        user = authenticate(request, username=email, password=password)
        # if credentials are not matched than redirect to login page
        if user is None:
            return render(request, "blog/login.html")
        login(request, user)
        return render(request, "blog/index.html")


class LogOut(RedirectView):
    """Logout View"""
    url = "/login/"

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOut, self).get(request, *args, **kwargs)
