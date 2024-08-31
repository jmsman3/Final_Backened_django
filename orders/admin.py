from django.contrib import admin
from .models import *
 #email
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives ,send_mail
# Register your models here.

# class OrderModelAdmin(admin.ModelAdmin):
    
#     def save_model(self,request,obj,form,change):
#         obj.save()

#         if obj.delivery_status:
#             email_subject = "Your Food Delivery Successfull"
#             email_body = render_to_string('deliver_email.html',
            
#                 {'user' : obj.user.user ,
#                 'total_price' :obj.total_price ,
#                 'order_date' : obj.order_date ,
#                 'Food_name' : obj.food_item.title ,
#                 'quantity' : obj.quantity ,
#                 'price':obj.price})
            
#             email = EmailMultiAlternatives(email_subject , '', to=[obj.user.user.email])
#             email.attach_alternative(email_body, "text/html")
#             email.send()

class OrderModelAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        obj.save()

        if obj.delivery_status:
            # Fetch all items in the order
            order_items = OrderItem.objects.filter(order=obj)

            # Calculate total price and get other details
            total_price = sum(item.price * item.quantity for item in order_items)
            # order_date = obj.created_at  # Assuming there's a created_at field in the Orders model
            user = obj.user

            # Create a list of food items
            food_items = [{'name': item.product.product_name, 'quantity': item.quantity, 'price': item.price} for item in order_items]

            # Render email template
            email_body = render_to_string(
                'deliver_email.html',
                {
                    'user': user.username,
                    'total_price': total_price,
                    # 'order_date': order_date,
                    'food_items': food_items,
                }
            )

            # Prepare and send email
            email_subject = "Your Food Delivery is Successful"
            email = EmailMultiAlternatives(
                subject=email_subject,
                body=email_body,
                to=[user.email]
            )
            email.attach_alternative(email_body, "text/html")
            email.send()


# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('order', 'product', 'quantity')
#     # Ensure the 'order' field is part of the fields shown in the admin form
#     fields = ('order', 'product', 'quantity')

admin.site.register(Cart)
admin.site.register(CartItems)

admin.site.register(Orders,OrderModelAdmin)
admin.site.register(OrderItem)

# admin.site.register(Cart_ItemModel)
# admin.site.register(ReviewModel)