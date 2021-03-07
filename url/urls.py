from django.urls import path

from . import views


app_name = "url"

urlpatterns = [
    path("", views.home, name="url-home"),
    path("<str:code>", views.redirect, name="url-redirect"),
    path("shortened/<str:code>", views.detail, name="url-detail"),
]
