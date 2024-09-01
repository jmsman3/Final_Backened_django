from django.shortcuts import render ,redirect
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializers ,RegistrationSerializer,UserLoginSerializer
from rest_framework.views import APIView
#add
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
#email
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives,send_mail
#authenticate
from .models import Profile
from django.contrib.auth import authenticate ,login,logout
from rest_framework.authtoken.models import Token
# Create your views here.
from rest_framework import filters,pagination 
#Filter
class SpecificPerson(filters.BaseFilterBackend):
    def filter_queryset(self,request , queryset , view):
        user_id   = request.query_params.get("user_id")
        if user_id  :
            print(f"Filtering by user_id: {user_id}")  #debug
            return queryset.filter(user__id=user_id)
        return queryset
    
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    filter_backends=[SpecificPerson]

    
    def perform_create(self, serializer):
        user_id = self.request.data.get('user')   #user id ta ber kore anlam 
        user = User.objects.get(id=user_id)  
        serializer.save(user=user)

class ProfileDetails(APIView):
    def get(self,request,id):
        user = User.objects.get(pk=id)
        Profileuser = Profile.objects.get(user=user) 
        serializer = ProfileSerializers(Profileuser)
        return Response(serializer.data)


    

class UserRegistrationApiView(APIView):
    serializer_class = RegistrationSerializer

    def post(self,request):
        serializer = self.serializer_class(data = request.data)
      
        if serializer.is_valid():
            user = serializer.save()
            Profile.objects.create(user=user)

            print(user)
            token = default_token_generator.make_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(uid)
            # confirm_link = f"https://food-project-9vo4.onrender.com/user/active/{uid}/{token}"
            # confirm_link = f"https://food-project-9vo4.onrender.com/user/active/{uid}/{token}"
            confirm_link = f"https://final-food-project.onrender.com/user/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check Your Email for Confirmation")
        return Response(serializer.errors)
    
def activate(request ,uid64,token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect('register')
    else:
        return redirect('register') 


class UserLoginApiView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data =self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username ,password=password)
            
            if user:
                token, _= Token.objects.get_or_create(user=user)
                print(_)
                login(request , user)
                return Response({'token' : token.key , 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)


class USerLogoutApiview(APIView):
    def get(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')

