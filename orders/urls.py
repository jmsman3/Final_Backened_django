from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *
router = DefaultRouter()


urlpatterns = [
    path('',include(router.urls)),
    path('cart', CartView.as_view()),
   
    path('order_now/',OrderView.as_view()),
]