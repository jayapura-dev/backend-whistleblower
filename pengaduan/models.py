from django.db import models
from django.utils.crypto import get_random_string
import uuid

class Distrik(models.Model):
    id_distrik = models.AutoField(primary_key=True)
    nama_distrik = models.CharField(max_length=50)
    kadis = models.CharField(max_length=100)
    sekdis = models.CharField(max_length=100)
    kotak_kadis = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_distrik


class Kampung(models.Model):
    id_kampung = models.AutoField(primary_key=True)
    distrik = models.ForeignKey(Distrik, on_delete=models.CASCADE)
    nama_kampung = models.CharField(max_length=100)
    kakam = models.CharField(max_length=100)
    sekam = models.CharField(max_length=100)
    kontak_kakam = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_kampung


class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=300)

    def __str__(self):
        return self.nama_kategori


class Aduan(models.Model):
    id_aduan = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    slug = models.SlugField(blank=True)
    nama_pengadu = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    no_telfon = models.CharField(max_length=13)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    distrik = models.ForeignKey(Distrik, on_delete=models.CASCADE)
    kampung = models.ForeignKey(Kampung, on_delete=models.CASCADE)
    deskripsi_aduan = models.CharField(max_length=250)
    file = models.FileField(upload_to='upload_doc/')
    date = models.DateTimeField(auto_now=False)
    status_aduan = models.CharField(max_length=15, blank=True)
    kode_unik = models.CharField(max_length=36, default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.title
