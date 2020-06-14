from .views import KategoriViewSets, DistrikViewSets, KampungViewSets, AduanViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'kategori', KategoriViewSets, basename='kategori')
router.register(r'distrik', DistrikViewSets, basename='distrik')
router.register(r'kampung', KampungViewSets, basename='kampung')
router.register(r'aduan', AduanViewSets, basename='aduan')

urlpatterns = router.urls