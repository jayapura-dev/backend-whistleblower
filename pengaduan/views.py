from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import models

def login(request):
    return render(request,'auth/login.html')

@login_required
def dashboard(request):
    contex = {
        'page_title': 'Dashboard | Admin'
    }

    return render(request,'admin/dashboard.html',contex)

@login_required
def datamaster(request):
    contex = {
        'page_title': 'Data Master | Admin'
    }

    return render(request, 'admin/data_master.html', contex);

@login_required
def aduan(request):
    contex = {
        'page_title': 'Aduan Masuk | Admin'
    }

    return render(request, 'aduan/r-aduan.html', contex);

@login_required
def distrik(request):
    contex = {
        'page_title': 'Distrik | Admin',
        'distrik': models.Distrik.objects.all()
    }

    return render(request, 'admin/r-distrik.html', contex);

@login_required
def kampung(request):
    contex = {
        'page_title': 'Kampung | Admin',
        'kampung': models.Kampung.objects.all()
    }

    return render(request, 'admin/r-kampung.html', contex);