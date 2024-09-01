from django.shortcuts import render ,redirect
from rest_framework import viewsets
from .models import Delivery
from .serializers import DeliverySerializers
from rest_framework.views import APIView

# Create your views here.


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializers




