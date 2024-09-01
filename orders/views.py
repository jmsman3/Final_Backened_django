from django.shortcuts import render
from rest_framework import viewsets
from menu.models import *
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters,pagination 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse

# Create your views here.

class CartView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request):
        user = request.user
        cart = Cart.objects.filter(user = user, ordered = False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        try:
            data = request.data
            user = request.user
            order, _ = Orders.objects.get_or_create(user=user, delivery_status=False)

            product = Product.objects.get(id=data.get('product'))
            price = product.price
            quantity = int(data.get('quantity'))

            order_item = OrderItem(order=order, user=user, product=product, price=price * quantity, quantity=quantity)
            order_item.save()

            # Update order total price
            order.total_price += order_item.price 
            order.save()

            return JsonResponse({'success': 'Order placed successfully'}, status=200)
        
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    # def post(self,request):
    #     data = request.data
    #     user = request.user
    #     cart,_ = Cart.objects.get_or_create(user = user, ordered = False)

    #     product = Product.objects.get(id= data.get('product'))
    #     price = product.price
    #     quantity = data.get('quantity')
    #     cart_items = CartItems(cart=cart , user=user,product=product,price=price,quantity=quantity)
    #     cart_items.save()

    #     total_price = 0
    #     cart_items = CartItems.objects.filter(user = user, cart=cart.id)
    #     for items in cart_items:
    #         total_price += items.price
    #     cart.total_price = total_price
    #     cart.save()

    #     return Response({'success' : 'Hey,Items Add Done to Cart'})
    
    # def post(self, request):
    #     data = request.data
    #     user = request.user
    #     cart, _ = Cart.objects.get_or_create(user=user, ordered=False)

    #     product = Product.objects.get(id=data.get('product'))
    #     quantity = int(data.get('quantity'))
    #     price = product.price * quantity

    #     cart_items = CartItems(cart=cart, user=user, product=product, price=price, quantity=quantity)
    #     cart_items.save()

    #     return Response({'success': 'Hey, Items Added to Cart'})



    def put(self,request):
        data= request.data
        
        cart_item = CartItems.objects.get(id = data.get('id'))
        quantity = int(data.get('quantity'))
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success' : 'Hey,Items Updated'})
        

    def delete(self,request):
        user = request.user
        data= request.data
        
        cart_item = CartItems.objects.get(id = data.get('id'))
        cart_item.delete()
        

        cart = Cart.objects.filter(user = user, ordered = False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializers(queryset,many=True)
        return Response(serializer.data)


class OrderView(APIView): 
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        user = request.user
        order = Orders.objects.filter(user=user, delivery_status=False).first()
        queryset = OrderItem.objects.filter(order=order)
        serializer = OrderItemsSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = request.user
        order, _ = Orders.objects.get_or_create(user=user, delivery_status=False)

        product = Product.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')

        order_item = OrderItem(order=order, user=user, product=product,  price=product.price*int(quantity), quantity=quantity)
        order_item.save()

        # Update the total amount after adding the new item
        self.update_order_amount(order)

        return Response({'success': 'Order Added to OrderCart'})

    def put(self, request):
        data = request.data
        order_item = OrderItem.objects.get(id=data.get('id'))
        quantity = int(data.get('quantity'))
        order_item.quantity += quantity
        order_item.save()

        # Update the total amount after updating the item
        self.update_order_amount(order_item.order)

        return Response({'success': 'Order Updated'})

    def delete(self, request):
        user = request.user
        data = request.data
        order_item = OrderItem.objects.get(id=data.get('id'))
        order = order_item.order
        order_item.delete()

        # Update the total amount after deleting the item
        self.update_order_amount(order)

        queryset = OrderItem.objects.filter(order=order)
        serializer = OrderItemsSerializers(queryset, many=True)
        return Response(serializer.data)

    def update_order_amount(self, order):
        order_items = OrderItem.objects.filter(order=order)
        total_amount = sum(item.price * item.quantity for item in order_items)
        order.amount = total_amount
        order.save()

# class CreateOrderView(APIView):
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class OrderListView(APIView):
#     def get(self, request):
#         orders = Orders.objects.filter(user=request.user)
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
