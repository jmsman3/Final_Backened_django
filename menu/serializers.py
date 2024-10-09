from rest_framework import serializers
from .models import *
from .image_utils import upload_image_to_imgbb
class CategorySerializers(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Category
        fields = '__all__'

# class ProductSerializers(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#     category = CategorySerializers()
#     class Meta:
#         model = Product
#         fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        # Extract the image from the validated data
        image = validated_data.pop('image', None)
        product = Product.objects.create(**validated_data)

        if image:
            # Upload image to ImgBB
            image_url = upload_image_to_imgbb(image)  # Call  upload function
            product.image = image_url  # Save the URL returned from ImgBB

        product.save()
        return product

    def update(self, instance, validated_data):
        # Extract the image if present
        image = validated_data.pop('image', None)

        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.stock = validated_data.get('stock', instance.stock)

        if image:
            # Upload new image to ImgBB
            image_url = upload_image_to_imgbb(image)
            instance.image = image_url  # Update the image URL

        instance.save()
        return instance


class Special_OfferSerializers(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = Special_Offer_Model
        fields = '__all__' 
