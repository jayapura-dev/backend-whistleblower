from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from django.urls import reverse_lazy
from django.views.generic import DetailView

from . import models
from .models import Kategori
from .forms import PostKategori

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

@login_required
def kategori(request):
    contex = {
        'page_title': 'Kategori Aduan | Admin',
        'kategori': models.Kategori.objects.all()
    }

    return render(request, 'admin/r-kategori.html', contex);

@login_required
def kategoripost(request):
    status = 'Berhasil Menambah Data'

    if request.method == 'POST':
        form = PostKategori(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('datamaster/kategori')
        else:
            form = PostKategori()
            return HttpResponseRedirect('datamaster/kategori')

@login_required
def kategoriedit(request):
    id_kategori = request.POST['id_kategori']
    kat = get_object_or_404(Kategori, pk=id_kategori)
    status = 'Item telah diupdate'

    if request.method == 'POST':
        form = PostKategori(request.POST, instance=kat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('datamaster/kategori')
        else:
            form = PostKategori()
            return HttpResponseRedirect('datamaster/kategori')
            

@login_required
def kategoridelete(request):
    id_kategori = request.POST['id_kategori']
    status = 'Item Telah dihapus'

    if request.method == 'POST':
        kat = Kategori.objects.get(pk=id_kategori)
        kat.delete()
        return HttpResponseRedirect('datamaster/kategori')


@login_required
def pengaduan(request):
    contex = {
        'page_title': 'Data Aduan Masuk | Admin',
        'pengaduan': models.Aduan.objects.all()
    }

    return render(request, 'aduan/r-aduan.html', contex);


@login_required
def petunjuk(request):
    contex = {
        'page_title': 'Petunjuk Pengisian Form Aduan',
        'petun': models.Petunjuk.objects.all()
    }

    return render(request, 'petunjuk/r-petunjuk.html', contex)


class detail_aduan(DetailView):
    template_name = 'aduan/rd-aduan.html'
    model = models.Aduan

    def get_context_data(self, **kwargs):
        page_title = 'Detail Aduan | Admin'
        context = super().get_context_data(**kwargs)
        return context

@login_required
def menajemen_user(request):
    contex = {
        'page_title': 'Users List',
    }

    return render(request, 'akun/menu.html', contex)

@login_required
def akun(request):
    contex = {
        'page_title': 'Users List',
        'user': User.objects.all()
    }

    return render(request, 'akun/r-akun.html', contex)