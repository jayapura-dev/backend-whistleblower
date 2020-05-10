from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request,'auth/login.html')
