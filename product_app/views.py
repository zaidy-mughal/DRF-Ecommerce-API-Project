from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Category, Brand
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
## these are already defined in settings.py file globally
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Category"])
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=["Brand"])
class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


@extend_schema(tags=["Product"])
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


