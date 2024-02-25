from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # Extract any fields that are not meant to be saved in the Product model
        # For example, if you have a field named 'extra_field' that is not part of the Product model
        extra_field = validated_data.pop('extra_field', None)

        # Create the Product instance using the remaining validated data
        product_instance = Product.objects.create(**validated_data)

        # You can perform additional operations here if needed

        return product_instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
