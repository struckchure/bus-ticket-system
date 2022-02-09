from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

from accounts.forms import UserRegisterForm, UserLoginForm


def user_register(request):
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()

            messages.error(request, "Invalid credentials")

            return redirect("tickets:bus-route-list")

    register_form = UserRegisterForm()

    context = {"register_form": register_form}
    template_name = "accounts/register.html"

    return render(request, template_name, context)


def user_login(request):
    next_url = request.GET.get("next", reverse("tickets:bus-route-list"))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(**login_form.cleaned_data)
            if user:
                login(request, user)

                return redirect(next_url)
            messages.error(request, "Invalid credentials")

    login_form = UserLoginForm()

    context = {"login_form": login_form}
    template_name = "accounts/login.html"

    return render(request, template_name, context)


def user_logout(request):
    logout(request)

    return redirect("accounts:login")
