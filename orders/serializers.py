from rest_framework import serializers
from .models import *
from menu.serializers import *
class CartSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields ='__all__'

class CartItemsSerializers(serializers.ModelSerializer):
    cart = CartSerializers()
    user = serializers.StringRelatedField()
    cart = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    product = ProductSerializers()
    class Meta:
        model = CartItems
        fields ='__all__'

# class OrderSerializer(serializers.ModelSerializer):
#     # user = serializers.StringRelatedField()
#     # product = serializers.StringRelatedField()
#     # product = ProductSerializers()
#     class Meta:
#         model = Orders
#         fields = ['id', 'user', 'delivery_status', 'product', 'amount', 'quantity']
#         read_only_fields = ['id', 'user'] 


class OrderSerializers(serializers.ModelSerializer):
    cart = CartSerializers()
    user = serializers.StringRelatedField()
    class Meta:
        model = Orders
        fields ='__all__'

class OrderItemsSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    cart = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    order = OrderSerializers()
    product = ProductSerializers()
    class Meta:
        model = OrderItem
        fields ='__all__'




# class ReviewModelSerializers(serializers.ModelSerializer):
#     user = serializers.StringRelatedField()
#     food_item = serializers.StringRelatedField()

#     class Meta:
#         model = ReviewModel
#         fields='__all__'