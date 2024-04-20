from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from business_app.models import (
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

class  OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['GET'])
    def pending(self, request):
        pending_order = Order.objects.filter(status_id__name = 'PENDING')
        serializer = self.get_serializer(pending_order, many=True)
        return Response(serializer.data)

class  OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
   