from django.contrib import admin
from .models import (
    Distrik,
    Kampung,
    Kategori,
    Aduan,
    Petunjuk
)

class tb_distrik(admin.ModelAdmin):
    list_display = ('id_distrik','nama_distrik','kadis','sekdis','kotak_kadis')
    list_display_links = ('id_distrik','nama_distrik','kadis','sekdis','kotak_kadis')
    search_fields = ('nama_distrik',)
    list_per_page = 10

class tb_kampung(admin.ModelAdmin):
    list_display = ('id_kampung','distrik','nama_kampung','kakam','sekam','kontak_kakam')
    list_display_links = ('id_kampung','distrik','nama_kampung','kakam','sekam','kontak_kakam')
    search_fields = ('nama_kampung',)
    list_per_page = 10
    list_filter = ('distrik',)

class tb_kategori(admin.ModelAdmin):
    list_display = ('id_kategori','nama_kategori','deskripsi')
    list_display_links = ('id_kategori','nama_kategori','deskripsi')
    search_fields = ('nama_kampung',)
    list_per_page = 10

class tb_aduan(admin.ModelAdmin):
    list_display = ('id_aduan','title','nama_pengadu','email','date')
    list_display_links = ('id_aduan','title','nama_pengadu','email','date')
    search_fields = ('title',)
    list_per_page = 10
    list_filter = ('date',)
    prepopulated_fields = {'slug': ('title', )}

class tb_petunjuk(admin.ModelAdmin):
    list_display = ('no','label','keterangan','sample')
    list_display_links = ('no','label','keterangan','sample')
    search_fields = ('label',)
    list_per_page = 10

admin.site.register(Distrik, tb_distrik)
admin.site.register(Kampung, tb_kampung)
admin.site.register(Kategori, tb_kategori)
admin.site.register(Aduan, tb_aduan)
admin.site.register(Petunjuk, tb_petunjuk)
