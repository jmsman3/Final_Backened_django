from django.contrib import admin
from .models import Delivery
# Register your models here.
class DelveryModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'deivery_status']
admin.site.register(Delivery ,DelveryModelAdmin)