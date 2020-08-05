from django.shortcuts import render
from rest_framework import generics, status, views
from .serializers import RegisterSerializer,EmailVerificationSerializer, LoginSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from .renderers import UserRenderer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .renderers import UserRenderer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
# Create your views here.

class RegisterView(generics.GenericAPIView):#Allows for User Registeration
    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hi '+user.username+ ' Use link below to verify your Email \n' + absurl
        data ={'email_body':email_body,'to_email':user.email, 'email_subject': 'Verify Your Email'}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED )
     
class VerifyEmail(views.APIView): # Verifies Email
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter('token',in_=openapi.IN_QUERY,description='Description',type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email':'Successfully Verified'}, status=status.HTTP_200_OK )

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error':'Activation Link Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error':'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(generics.GenericAPIView): #Login Api View
    serializer_class=LoginSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RequestPasswordResetEmail(generics.GenericAPIView): #This sends suser email and validates if user is registered to the database
    serializer_class=ResetPasswordEmailRequestSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user) 
            current_site = get_current_site(
            request=request).domain
            relativeLink = reverse('password-reset-confirm',kwargs={'uidb64':uidb64, 'token':token})
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hi '+user.username+ ' Hello, \n Use link below to Reset you Password \n' + absurl
            data ={'email_body':email_body,'to_email':user.email, 'email_subject': 'Reset Your Password'}
            Util.send_email(data)
            return Response({'Success':'We have sent you a link to reset your password'},status=status.HTTP_200_OK)
        else:
            return Response({'Error':'You do not have an account registered'},status=status.HTTP_400_BAD_REQUEST)
        
class PasswordTokenCheckAPI(generics.GenericAPIView): #checks if Token is Valid
    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token): # This ensures that user is not re-using the resetlink
                return Response({'Error':'Token is not valid, please request a new one'},status=status.HTTP_401_UNAUTHORIZED)
        
            return Response({'Success':True, 'Message':'Credentials Valid','uidb64':uidb64, 'Token':token},status=status.HTTP_200_OK)

            
        except DjangoUnicodeDecodeError as identifier: #This handles erros, for example if the user, tampers with the token.
            return Response({'Error':'Token is not valid, please request a new one'},status=status.HTTP_401_UNAUTHORIZED)

class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self,request):# We use patch, because we are changing the Users Password
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'Success':True, 'Message':'Password Reset Success'},status=status.HTTP_200_OK)
