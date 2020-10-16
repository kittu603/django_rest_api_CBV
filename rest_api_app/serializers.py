from .models import Product
from rest_framework import serializers


# created a serializer which converts my model and what fields to convert from my model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


