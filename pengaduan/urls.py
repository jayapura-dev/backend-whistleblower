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
    path('', include('akun.urls')),

    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('datamaster', views.datamaster, name='datamaster'),
    path('datamaster/distrik', views.distrik, name='distrik'),
    path('datamaster/kampung', views.kampung, name='kampung'),
    path('datamaster/kategori', views.kategori, name='kategori'),
    
    path('postkategori', views.kategoripost, name='postkategori'),
    path('editkategori', views.kategoriedit, name='editkategori'),
    path('deletekategori', views.kategoridelete, name='deletekategori'),
    path('pengaduan', views.pengaduan, name='pengaduan'),
    path('pengaduan/detail/<int:pk>/', detail_aduan.as_view(), name='detail'),
    path('petunjuk', views.petunjuk, name='petunjuk'),

    path('menajemen_user', views.menajemen_user, name='menajemen_user'),
    path('menajemen_user/akun', views.akun, name='akun'),
]