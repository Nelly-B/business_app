from rest_framework import serializers
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from user_app.models import CustomUser
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from business_app.models import (
    Customer,
    Product,
    Unit_of_measurment,
    Status,
    Order,
    OrderItem,
    )

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


    def create(self, validated_data):
        customer = Customer.objects.create(**validated_data)
        username = validated_data['username']
        email = validated_data['email']
        password = email.split('@')[0]

        if customer is not None:
            user = CustomUser.objects.create(
                username=username,
                email=email
            )
            user.set_password(password)
            user.save()

            data = {
                'customer': customer,
                'email': email,
                'login_details': {
                    'username': username,
                    'password': password
                }
            }
            print(data)
            send_mail(
                subject='Welcome',
                message='Welcome to our service!',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],  # Using the provided email
                fail_silently=False,
            )
            
        return customer
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


    # def create(self, validated_data):
    #     if validated_data.get('quantity', 0) == 0:
    #         product_status = Status.objects.filter(name='Out of Stock')
    #     else:
    #         product_status = Status.objects.filter(name='In Stock')

    #     validated_data['status'] = product_status
    #     return super().create(validated_data)

    def create(self, validated_data):
        quantity = validated_data.get('quantity', 0)
        if quantity == 0:
            product_status = Status.objects.filter(name='Out of Stock')[0]
        else:
            product_status = Status.objects.filter(name='In Stock')[0]

        validated_data['status'] = product_status
        return super().create(validated_data)
            
        
class Unit_of_measurment_Serializer(serializers.ModelSerializer):
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
        fields = ['id', 'name']

class  InstockSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    message = serializers.CharField(max_length=20)
        