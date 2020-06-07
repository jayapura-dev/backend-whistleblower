from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views
from . views import (
    detail_aduan,
)

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('datamaster', views.datamaster, name='datamaster'),
    path('datamaster/distrik', views.distrik, name='distrik'),
    path('datamaster/kampung', views.kampung, name='kampung'),
    path('pengaduan', views.aduan, name='pengaduan'),
    path('pengaduan/detail/<slug:slug>/', detail_aduan.as_view(), name='detail'),
]