from django.contrib import admin
from user_app.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from user_app.serializer import CustomUserSerializer

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    serializer_class = CustomUserSerializer
    model = CustomUser
    list_display = ['email', 'username']

