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
        if not order:
            return Response({'error': 'No active order found'}, status=404)

        queryset = OrderItem.objects.filter(order=order)
        serializer = OrderItemsSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = request.user
        order, _ = Orders.objects.get_or_create(user=user, delivery_status=False)

        try:
            product = Product.objects.get(id=data.get('product'))
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)

        quantity = int(data.get('quantity', 0))
        if quantity <= 0:
            return Response({'error': 'Invalid quantity'}, status=400)

        if product.stock < quantity:
            return Response({'error': 'Insufficient stock'}, status=400)

        # Create or update the order item
        order_item, created = OrderItem.objects.get_or_create(
            order=order, product=product,
            defaults={'quantity': quantity, 'price': product.price * quantity}
        )
        if not created:
            order_item.quantity += quantity
            order_item.price = product.price * order_item.quantity  # Ensure price reflects total cost
            order_item.save()

        product.stock -= quantity  # Deduct stock
        product.save()

        self.update_order_amount(order)

        return Response({'success': 'Order added to cart'})

    def put(self, request):
        data = request.data
        try:
            order_item = OrderItem.objects.get(id=data.get('id'))
        except OrderItem.DoesNotExist:
            return Response({'error': 'Order item not found'}, status=404)

        quantity = int(data.get('quantity', 0))
        if quantity <= 0:
            return Response({'error': 'Quantity must be greater than 0'}, status=400)

        if order_item.product.stock < quantity:
            return Response({'error': 'Insufficient stock'}, status=400)

        # Update quantity and price
        order_item.quantity = quantity
        order_item.price = order_item.product.price * quantity  # Ensure price reflects total cost
        order_item.save()

        self.update_order_amount(order_item.order)

        return Response({'success': 'Order updated'})

    def delete(self, request):
        data = request.data
        try:
            order_item = OrderItem.objects.get(id=data.get('id'))
        except OrderItem.DoesNotExist:
            return Response({'error': 'Order item not found'}, status=404)

        order = order_item.order
        order_item.delete()

        self.update_order_amount(order)

        queryset = OrderItem.objects.filter(order=order)
        serializer = OrderItemsSerializers(queryset, many=True)
        return Response(serializer.data)

    def update_order_amount(self, order):
        order_items = OrderItem.objects.filter(order=order)
        total_amount = sum(item.price for item in order_items)
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
