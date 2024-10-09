# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import *
# from rest_framework import filters,pagination 
# from .serializers import *
# from rest_framework.views import APIView
# from rest_framework.response import Response


# class ProductView(APIView):
    
#     def get(self,request):
#         category_id = self.request.query_params.get('category_id')
#         if category_id:
#             queryset = Product.objects.filter(category_id=category_id)
#         else:
#             queryset = Product.objects.all()
#         # print(category)

#         serializer = ProductSerializers(queryset,many=True)
#         # print(serializer)
#         return Response({'count' : len(serializer.data) , 'data' : serializer.data})
    
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializers
from .image_utils import upload_image_to_imgbb  # Import your upload function

class ProductView(APIView):

    def get(self, request):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = Product.objects.filter(category_id=category_id)
        else:
            queryset = Product.objects.all()

        serializer = ProductSerializers(queryset, many=True)
        return Response({'count': len(serializer.data), 'data': serializer.data})

    def post(self, request):
        # Check if an image file is provided
        image_file = request.FILES.get('image')  # Assuming 'image' is the key in the form data
        
        # Upload the image to ImgBB if an image file is provided
        if image_file:
            image_url = upload_image_to_imgbb(image_file)
            if not image_url:
                return Response({"error": "Image upload failed."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            image_url = None  # Or handle this case as per your requirement

        # Prepare the data for the serializer
        product_data = {
            'category': request.data.get('category'),
            'product_name': request.data.get('product_name'),
            'image': image_url,  # Use the uploaded image URL
            'price': request.data.get('price'),
            'description': request.data.get('description'),
            'stock': request.data.get('stock'),
        }

        # Create the product instance
        serializer = ProductSerializers(data=product_data)
        
        if serializer.is_valid():
            serializer.save()  # Save the product with the image URL
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
