from rest_framework import serializers
from .models import Product, Review, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True, required=False)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description','category', 'price', 'avg_rating']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
