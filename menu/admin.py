from django.contrib import admin
from .models import *
# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    prepopulated_fields ={"slug": ("category_name",),}
admin.site.register(Category,CategoryModelAdmin)


# class FoodItemModelAdmin(admin.ModelAdmin):
#     list_display = ['title','price_with_taka_poisa_sign','image','description','category']

#     def price_with_taka_poisa_sign(self,obj):
#         return f"$ {obj.price}"
admin.site.register(Product)

# class SpecialOfferModel(admin.ModelAdmin):
#     list_display = ['food_item','discount_show','start_date','end_date']

#     def discount_show(self,obj):
#         return f"{obj.discount_percentage} % Off, On {obj.food_item}"
admin.site.register(Special_Offer_Model)
