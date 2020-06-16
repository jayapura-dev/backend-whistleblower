from ..models import Kategori, Distrik, Kampung, Aduan, Petunjuk
from .serializers import KategoriSerialiers, DistrikSerializers, KampungSerializers, AduanSerializers, PetunjukSerializers, SearchAduanSerializers
from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['kode_unik']

class PetunjukViewSets(viewsets.ModelViewSet):
    serializer_class = PetunjukSerializers
    queryset = Petunjuk.objects.all()

class SearchAduanViewSets(viewsets.GenericViewSet):
    serializer_class = SearchAduanSerializers
    queryset = Aduan.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['kode_unik']