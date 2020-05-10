from django.db import models

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
