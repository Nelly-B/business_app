from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    phone_number = PhoneNumberField(max_length = 50, unique=True, null=False)
    address = models.CharField(max_length=225)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

class Status(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'status'

    def __str__(self):
        return f"{self.user}"


class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='media', default='jpg', null=True)
    quantity = models.IntegerField(default=0)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table ='products'

    def __str__(self):
        return f"{self.name} {self.quantity}"

class Unit_of_measurment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=225)
    unit = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class  Meta:
        db_table = 'unit_of_measurement'

    def __str__(self):
        return f"{self.product} {self.price}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_of_measurement = models.ForeignKey(Unit_of_measurment, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"{self.user}"

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    subtotal = models.IntegerField()

    class Meta:
        db_table = 'order_Items'

    def __str__(self):
        return f"{self.quantity}"

