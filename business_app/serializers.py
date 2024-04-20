from rest_framework import serializers
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from business_app.models import (
    Customer,
    Product,
    Unit_of_measurment,
    Status,
    Order,
    OrderItem,
    User
    )

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
   

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

        
class UmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit_of_measurment
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class  InstockSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    message = serializers.CharField(max_length=20)
        