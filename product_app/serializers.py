from rest_framework import serializers
from .models import Category, Product, Brand
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'products']




class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField()
    class Meta:
        model = Category
        fields = ['id','name','parent']



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer(read_only=True)
    # category = CategorySerializer(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = "__all__"
