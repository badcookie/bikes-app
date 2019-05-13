from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product, Manager, Category
from .serializers import (
    ProductSerializer,
    CategoryProductSerializer,
    PublicProductSerializer,
    PublicCategoryProductSerializer,
)


class PublicProductListPagination(PageNumberPagination):
    page_size = 5


class ProductViewSet(viewsets.ModelViewSet):
    """Defines actions and queries accessible to managers only."""

    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        return (
            CategoryProductSerializer
            if self.action == 'category'
            else ProductSerializer
        )

    def get_queryset(self):
        """Collects all products for manager's company.

        Returns
        -------
            Products queryset.

        """

        manager = Manager.objects.get(user=self.request.user)
        products = Product.objects.filter(company=manager.company)
        return products

    def perform_create(self, serializer):
        """Creates a product instance from manager's company.

        Parameters
        ----------
        serializer

        Returns
        -------
            Product instance with valid data.

        """

        category_id = self.request.data['category']
        category = get_object_or_404(Category, id=category_id)
        manager = Manager.objects.get(user=self.request.user)
        serializer.save(company=manager.company, category=category)

    def update(self, request, *args, **kwargs):
        """Modifies product instance fully or partially.

        Parameters
        ----------
        request
        args
        kwargs

        Returns
        -------
            Product's modified data.

        """

        product = self.get_object()
        fields_to_update = request.data
        for field, value in fields_to_update.items():
            setattr(product, field, value)
        product.save()
        updated_product = self.get_serializer(product).data
        return Response(updated_product)

    @action(methods=['get'], detail=False, url_path='category/(?P<pk>[^/.]+)')
    def category(self, request, pk):
        """Nested route to get list of company's products for a particular category.

        Parameters
        ----------
        request
        pk
            Category id.

        Returns
        -------
            Products list.

        """

        category = get_object_or_404(Category, id=pk)
        category_products = self.get_queryset().filter(category=category)
        category_products_list = [
            self.get_serializer(item).data for item in category_products
        ]
        return Response(category_products_list)


class PublicProductViewSet(viewsets.ModelViewSet):
    """Defines actions and queries accessible to all users."""

    http_method_names = ['get']
    permission_classes = (permissions.AllowAny,)
    pagination_class = PublicProductListPagination
    queryset = Product.objects.all()

    def get_serializer_class(self):
        return (
            PublicCategoryProductSerializer
            if self.action == 'category'
            else PublicProductSerializer
        )

    @action(methods=['get'], detail=False, url_path='category/(?P<pk>[^/.]+)')
    def category(self, request, pk):
        """Nested route to get list of all products for a particular category.

        Parameters
        ----------
        request
        pk
            Category id.

        Returns
        -------
            Paginated products list.

        """

        category = get_object_or_404(Category, id=pk)
        category_products = self.get_queryset().filter(category=category)
        products_per_page = self.paginate_queryset(category_products)
        category_products_list = [
            self.get_serializer(item).data for item in products_per_page
        ]
        return self.get_paginated_response(category_products_list)
