from ..models import Kategori, Distrik, Kampung, Aduan
from .serializers import KategoriSerialiers, DistrikSerializers, KampungSerializers, AduanSerializers
from rest_framework import viewsets

class KategoriViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = KategoriSerialiers
    queryset = Kategori.objects.all()

class DistrikViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = DistrikSerializers
    queryset = Distrik.objects.all()

class KampungViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = KampungSerializers
    queryset = Kampung.objects.all()

class AduanViewSets(viewsets.ModelViewSet):
    serializer_class = AduanSerializers
    queryset = Aduan.objects.all()