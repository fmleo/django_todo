from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm


class Register(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/register.html"


class Login(LoginView):
    success_url = reverse_lazy("home")
    template_name = "accounts/login.html"


class Logout(LogoutView):
    next_page = reverse_lazy("home")
