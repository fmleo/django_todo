from django.urls import path

from .views import Login, Logout, Register

app_name = "accounts"
urlpatterns = [
    path("registrar/", Register.as_view(), name="register"),
    path("entrar/", Login.as_view(), name="login"),
    path("desconectar/", Logout.as_view(), name="logout"),
]
