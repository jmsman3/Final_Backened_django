from rest_framework import serializers
from .models import Delivery
from django.contrib.auth.models import User
class DeliverySerializers(serializers.ModelSerializer):
    deivery_status = serializers.StringRelatedField(many=False)
    class Meta:
        model = Delivery
        fields = '__all__'
