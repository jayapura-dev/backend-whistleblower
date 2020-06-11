from rest_framework import serializers
from ..models import Distrik, Kampung, Kategori, Aduan

class DistrikSerializers(serializers.ModelSerializer):
    class Meta:
        model = Distrik
        fields = ('id_distrik','nama_distrik','kadis','sekdis','kotak_kadis')


class KampungSerializers(serializers.ModelSerializer):
    distrik = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Kampung
        fields = ('id_kampung','distrik','nama_kampung','kakam','sekam','kontak_kakam')


class KategoriSerialiers(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ('id_kategori','nama_kategori','deskripsi')