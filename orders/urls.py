from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import *
# from .views import Cart_itemViewSet,OrderViewSet,ReviewViewSet
router = DefaultRouter()

# router.register('cart_item' , Cart_itemViewSet) #router er antena

# router.register('food_order' , OrderViewSet) #router er antena
# router.register('review' , ReviewViewSet) #router er antena
urlpatterns = [
    path('',include(router.urls)),
    path('cart', CartView.as_view()),
    # path('order_now',CreateOrderView.as_view()),
    # path('order_list',OrderListView.as_view()),
    path('order_now',OrderView.as_view()),
]