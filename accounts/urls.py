from django.urls import path

from accounts.views import user_login, user_logout, user_register

app_name = "accounts"

urlpatterns = [
    path("register/", user_register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]
