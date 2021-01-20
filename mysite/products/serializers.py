from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Products
        fields = ['id', 'code', 'name', 'specification', 'size', 'singular_unit', 'plural_unit', 'package_quantity',
                  'image', 'category']
