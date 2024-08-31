from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200 ,default="")
    location = models.CharField(max_length=100,blank=True ,default="")
    mobile_no = models.CharField(max_length=12 ,default="")
    image = models.CharField(max_length=12 , default="" )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    class Meta:
        verbose_name_plural = "Profile User"