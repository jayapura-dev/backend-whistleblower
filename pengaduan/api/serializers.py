from rest_framework import serializers
from ..models import Distrik, Kampung, Kategori, Aduan

class KampungSerializers(serializers.ModelSerializer):

    class Meta:
        model = Kampung
        fields = ('distrik','id_kampung','nama_kampung')

class DistrikSerializers(serializers.ModelSerializer):
    kampungs = KampungSerializers(many=True, read_only=True)

    class Meta:
        model = Distrik
        fields = ('id_distrik','nama_distrik','kampungs')


class KategoriSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ('id_kategori','nama_kategori','deskripsi')

class AduanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aduan
        fields = (
            'id_aduan',
            'title',
            'slug',
            'nama_pengadu',
            'email',
            'no_telfon',
            'kategori',
            'distrik',
            'kampung',
            'deskripsi_aduan',
            'file',
            'date',
            'status_aduan',
            'kode_unik'
        )