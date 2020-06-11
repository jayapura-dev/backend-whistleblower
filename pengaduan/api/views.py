from ..models import Kategori, Distrik, Kampung
from .serializers import KategoriSerialiers, DistrikSerializers, KampungSerializers
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