from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views
router = DefaultRouter()

router.register('status' , views.DeliveryViewSet) #router er antena

urlpatterns = [
    path('',include(router.urls)),
    
]
