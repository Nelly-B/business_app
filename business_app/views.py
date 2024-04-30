from django.shortcuts import render
from rest_framework import viewsets, status
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from business_app.models import (
    Unit_of_measurment,
    Customer,
    Product,
    Order,
    OrderItem,
    Status,
    
)
from business_app.serializers import (
    ProductSerializer,
    CustomerSerializer,
    StatusSerializer,
    OrderSerializer,
    OrderItemSerializer,
    InstockSerializer,
    Unit_of_measurment_Serializer,
)

# Create your views here.

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail = True, methods = ['GET'], url_path='instock/(?P<quantity>[^/.]+)')
    def instock(self, request, **kwargs):
        print(f'args = {request}')
        print(f'kwargs = {kwargs}')
        product = Product.objects.get(pk = int(kwargs['pk']))
        if product.quantity == 0:
            return Response(message='Out of Stock')
        if product.quantity < int(kwargs['quantity']):
             return Response(f'Available quantity is {product.quantity}')
        
        return Response(True)
    
    def delete(self, request, *args, **kwargs):
        logedin_user = request.user
        if (logedin_user == 'admin'):
            product = self.get_object()
            product.delete()
            response_message = {"message": "Product has been deleted"}
        else:
            response_message = {'message': 'Product can not be deleted'}

        return Response(response_message, status=status.HTTP_204_NO_CONTENT)

class  OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    # @receiver(post_save, sender=Order)
    # def update_order_status(sender, instance, created, **kwargs):
    #     if created:
    #         instance.status = 'awaiting_delivery'
    #         instance.save()

    
    # @action(detail=False, methods=['GET'])
    # def pending(self, request):
    #     pending_order = Order.objects.filter(status_id__name = 'Awaiting delivery').count()
    #     serializer = self.get_serializer(pending_order, many=True)
    #     return Response(serializer.data)

class  OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class Unit_of_measurement_viewSet(viewsets.ModelViewSet):
    queryset = Unit_of_measurment.objects.all()
    serializer_class = Unit_of_measurment_Serializer()
   