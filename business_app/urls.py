from rest_framework.routers import DefaultRouter
from business_app.views import (
    ProductViewSet,
    OrderItemViewSet,
    CustomerViewset,
    OrderViewSet,
    StatusViewSet,
    UserCreateViewSet
)
router = DefaultRouter()
router.register(r'customer', CustomerViewset, basename='customer'),
router.register(r'product', ProductViewSet, basename='product'),
router.register(r'order', OrderViewSet, basename='order'),
router.register(r'orderItem', OrderItemViewSet, basename='orderItem'),
router.register(r'status', StatusViewSet, basename='status'),
router.register(r'create_user', UserCreateViewSet, basename='user')

urlpatterns = []

urlpatterns += router.urls
