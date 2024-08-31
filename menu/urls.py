from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *
router = DefaultRouter()

# router.register('category' , CategoryViewSet) #router er antena
# router.register('food-item-list' , ProductView) #router er antena
# router.register('special-offer' , Special_OfferViewSet) #router er antena
urlpatterns = [
    path('',include(router.urls)),
    path('products/', ProductView.as_view(), name='product-list'),

]
