from .views import KategoriViewSets, DistrikViewSets, KampungViewSets, AduanViewSets, PetunjukViewSets, SearchAduanViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'kategori', KategoriViewSets, basename='kategori')
router.register(r'distrik', DistrikViewSets, basename='distrik')
router.register(r'kampung', KampungViewSets, basename='kampung')
router.register(r'aduan', AduanViewSets, basename='aduan')
router.register(r'petunjuk', PetunjukViewSets, basename='petunjuk')
router.register(r'searchaduan', SearchAduanViewSets, basename='searchaduan')

urlpatterns = router.urls