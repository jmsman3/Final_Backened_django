from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework import filters,pagination 
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = CategoryModel.objects.all()
#     serializer_class = CategorySerializers

# #Pagination
# class Food_Item_Pagination(pagination.PageNumberPagination):
#     page_size = 1 #items per page
#     page_size_query_param = page_size
#     max_page_size = 100

# #Filter
# class Food_Item_ForSpecificCategory(filters.BaseFilterBackend):
#     def filter_queryset(self,request , query_set,view):
#         category_id  = request.query_params.get("category_id")
#         if category_id :
#             return query_set.filter(category__id=category_id)
#         return query_set
 
    
# class Food_itemViewSet(viewsets.ModelViewSet):
#     queryset = Food_item_Model.objects.all()
#     serializer_class = Food_itemSerializers

#     # pagination_class = Food_Item_Pagination
#     filter_backends = [Food_Item_ForSpecificCategory]


# class Special_OfferViewSet(viewsets.ModelViewSet):
#     queryset = Special_Offer_Model.objects.all()
#     serializer_class = Special_OfferSerializers


class ProductView(APIView):
    
    def get(self,request):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = Product.objects.filter(category_id=category_id)
        else:
            queryset = Product.objects.all()
        # print(category)

        serializer = ProductSerializers(queryset,many=True)
        # print(serializer)
        return Response({'count' : len(serializer.data) , 'data' : serializer.data})
    
