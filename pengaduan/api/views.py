from ..models import Kategori, Distrik, Kampung, Aduan, Petunjuk
from .serializers import KategoriSerialiers, DistrikSerializers, KampungSerializers, AduanSerializers, PetunjukSerializers, SearchAduanSerializers
from rest_framework import viewsets, filters, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class KategoriViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = KategoriSerialiers
    queryset = Kategori.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class DistrikViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = DistrikSerializers
    queryset = Distrik.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class KampungViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = KampungSerializers
    queryset = Kampung.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class AduanViewSets(viewsets.ModelViewSet):
    serializer_class = AduanSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['kode_unik']
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        return self.request.user.useraduan.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class PetunjukViewSets(viewsets.ReadOnlyModelViewSet):
    serializer_class = PetunjukSerializers
    queryset = Petunjuk.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]

class SearchAduanViewSets(viewsets.GenericViewSet):
    serializer_class = SearchAduanSerializers
    queryset = Aduan.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['kode_unik']
    permission_classes = [
        permissions.IsAuthenticated,
    ]