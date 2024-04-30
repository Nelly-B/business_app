from django.contrib import admin
from business_app.models import Status, Product, Customer, Order, OrderItem

# Register your models here.
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'quantity', 'status']
    list_filter = ['name', 'quantity']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'address', 'email', 'username' ]
    list_filter = ['first_name', 'last_name', 'email', 'username']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_id', 'unit_of_measurement', 'status']

@admin.register(OrderItem)
class OderItemAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product_id', 'quantity', 'unit_price', 'subtotal']