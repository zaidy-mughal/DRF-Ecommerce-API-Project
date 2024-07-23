from rest_framework import serializers
from .models import Category, Product, Brand, ProductImage, ProductLine


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
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = "__all__"


class ProductLineSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = ProductLine
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    product_line = ProductLineSerializer()
    class Meta:
        model = ProductImage
        fields = '__all__'