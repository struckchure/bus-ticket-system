"""
bus_ts Root URL Configuration
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from django.shortcuts import redirect


def index_redirect(_):
    return redirect("tickets:bus-route-list")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_redirect),
    path("accounts/", include("accounts.urls")),
    path("tickets/", include("tickets.urls")),
]
