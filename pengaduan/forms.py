from django.forms import ModelForm
from .models import Kategori, Distrik, Kampung, Aduan

class PostKategori(ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama_kategori','deskripsi']

class PostDistrik(ModelForm):
    class Meta:
        model = Distrik
        fields = ['nama_distrik','kadis','sekdis','kotak_kadis']

class PostKampung(ModelForm):
    class Meta:
        model = Kampung
        fields = ['distrik','nama_kampung','kakam','sekam','kontak_kakam']
