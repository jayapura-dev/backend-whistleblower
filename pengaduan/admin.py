from django.contrib import admin
from .models import (
    Distrik,
    Kampung
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

admin.site.register(Distrik, tb_distrik)
admin.site.register(Kampung, tb_kampung)