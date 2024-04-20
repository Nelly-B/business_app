from rest_framework.routers import DefaultRouter
from django.urls import path
from user_app.views import UserCreateViewSet
from business_app.views import (
    ProductViewSet,
    OrderItemViewSet,
    CustomerViewset,
    OrderViewSet,
    StatusViewSet,
)
router = DefaultRouter()
router.register(r'customer', CustomerViewset, basename='customer'),
router.register(r'product', ProductViewSet, basename='product'),
router.register(r'order', OrderViewSet, basename='order'),
router.register(r'orderItem', OrderItemViewSet, basename='orderItem'),
router.register(r'status', StatusViewSet, basename='status'),
router.register(r'register', UserCreateViewSet, basename='user')
# router.register(r'login', user_login, basename='user_login')

urlpatterns = []

urlpatterns += router.urls
