from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField() # Если в поле category нужно не название, а id, то удали эту строку

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price',
                  'category', 'imageUrl', 'stock')
