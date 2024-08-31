from rest_framework import serializers
from .models import *
class CategorySerializers(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    category = CategorySerializers()
    class Meta:
        model = Product
        fields = '__all__'

class Special_OfferSerializers(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = Special_Offer_Model
        fields = '__all__' 
