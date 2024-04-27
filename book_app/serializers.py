from rest_framework import serializers
from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model
    """
    class Meta:
        model = Book
        fields = '__all__'
