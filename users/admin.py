from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['first_name' ,'last_name' ,'bio','mobile_no','image','location']

    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name
admin.site.register(Profile ,ProfileAdminModel) 
