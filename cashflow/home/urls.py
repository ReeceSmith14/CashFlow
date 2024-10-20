from django.contrib import admin
from django.urls import path, include
from . import views
from .views import custom_login_redirect

urlpatterns = [
    path('', views.index, name='home'),
    path('login-redirect/', custom_login_redirect, name='custom_login_redirect'),
]
