from django.shortcuts import render
from user_app.serializer import CustomUserSerializer
from user_app.models import CustomUser
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

class UserCreateViewSet(viewsets.ModelViewSet):
    queryset =CustomUser.objects.all()
    serializer_class =CustomUserSerializer
    permission_classes=[IsAuthenticated]
    parser_classes=[MultiPartParser, FormParser]

