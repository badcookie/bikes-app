from django.urls import include, path
from .views import ProductViewSet, PublicProductViewSet, CategoriesViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


user_routes = [
    path('', PublicProductViewSet.as_view({'get': 'list'})),
    path('<int:product_id>/', PublicProductViewSet.as_view({'get': 'retrieve'})),
    path('category/<int:category_id>/', PublicProductViewSet.as_view({'get': 'list'})),
]

manager_routes = [
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path(
        '<int:product_id>/',
        ProductViewSet.as_view(
            {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
        ),
    ),
    path('category/<int:category_id>/', ProductViewSet.as_view({'get': 'list'})),
]

urlpatterns = [
    path('products/', include(user_routes)),
    path('company/products/', include(manager_routes)),
    path('categories/', CategoriesViewSet.as_view({'get': 'list'})),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
]
