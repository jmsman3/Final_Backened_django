from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Delivery(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    deivery_status = models.BooleanField(default=False) 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)

