from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views
router = DefaultRouter()

router.register('list' , views.ProfileViewSet) #router er antena


urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.UserRegistrationApiView.as_view(),name="register"),
    path('login/',views.UserLoginApiView.as_view(),name="login"),
    path('logout/',views.USerLogoutApiview.as_view(),name="logout"),
    path('active/<uid64>/<token>/' ,views.activate, name='active'),
    path('user_details/<int:id>/' ,views.ProfileDetails.as_view(), name='user_Details'),

]
