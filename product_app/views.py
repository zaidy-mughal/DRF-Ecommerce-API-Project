from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Product, Category, Brand
#this is used to get django build in model User.
from django.contrib.auth.models import User
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer, UserSerializer
from drf_spectacular.utils import extend_schema
from .pagination import CustomPagination
## these are already defined in settings.py file globally
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly,DjangoModelPermissionsOrAnonReadOnly
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
# from rest_framework.filters import SearchFilter,OrderingFilter

@extend_schema(tags="UserList")
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



@extend_schema(tags="User")
class UserRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



@extend_schema(tags=["Category"])
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    ordering_fields = ['name']
    search_fields = ['name']
    pagination_class = CustomPagination
    


@extend_schema(tags=["Brand"])
class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    search_fields = ['name']
    ordering_fields = ['name']
    pagination_class = CustomPagination



@extend_schema(tags=["Product"])
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['name']
    ordering_fields = '__all__'
    pagination_class = CustomPagination
