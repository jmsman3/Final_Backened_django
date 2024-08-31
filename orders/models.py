from django.db import models
from django.contrib.auth.models import User
from users.models import *
from menu.models import *
from delivery.models import *
# from delivery.models import Delivery
# from .constant import STAR_CHOICES
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# # Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username} | total price- {self.total_price}"
    class Meta:
        verbose_name_plural = 'Cart'

class CartItems(models.Model):
    cart = models.ForeignKey(Cart,  on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user.username)+ ' '+str(self.product.product_name)
    class Meta:
        verbose_name_plural = 'Cart Items'


@receiver(pre_save, sender=CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = float(cart_items.quantity) * float(price_of_product.price)
    print(f"Updated price: {cart_items.price}") 

    # total_cart_items = CartItems.objects.filter(user = cart_items.user)
    # cart =Cart.objects.get(id = cart_items.cart.id)
    # cart.total_price = cart_items.price
    # cart.save()




class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    delivery_status = models.BooleanField(default=False)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    # quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name_plural = "Orders"

class OrderItem(models.Model):
    user = models.ForeignKey(User, related_name='items' , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
   

    def __str__(self):
        return f"{self.user.username} - Order #{self.order.id}"


@receiver(post_save, sender=OrderItem)
def update_order_amount(sender, instance, **kwargs):
    order = instance.order
    order_items = OrderItem.objects.filter(order=order)
    total_amount = sum(item.price for item in order_items)
    order.amount = total_amount
    order.save() 




# class ReviewModel(models.Model):                
#     user = models.ForeignKey(Profile , on_delete=models.CASCADE)
#     food_item = models.ForeignKey(Product,on_delete=models.CASCADE)
#     rating = models.CharField(choices=STAR_CHOICES , max_length=12)
#     comment = models.TextField()
#     created_date = models.DateField(auto_now_add=True)

#     def  __str__(self):
#         return f"Review by {self.user.user.first_name} {self.user.user.last_name} on {self.food_item.title}"
#     class Meta:
#         verbose_name_plural='Reviews'

