from .views import KategoriViewSets, DistrikViewSets, KampungViewSets
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'kategori', KategoriViewSets, basename='kategori')
router.register(r'distrik', DistrikViewSets, basename='distrik')
router.register(r'kampung', KampungViewSets, basename='kampung')

urlpatterns = router.urls