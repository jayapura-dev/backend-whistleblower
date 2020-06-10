from django.forms import ModelForm
from .models import Kategori

class PostKategori(ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama_kategori','deskripsi']