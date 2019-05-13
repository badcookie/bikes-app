from .views import ProductViewSet, PublicProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('company/products', ProductViewSet, basename='product')
router.register('products', PublicProductViewSet, basename='public-product')

urlpatterns = router.urls
