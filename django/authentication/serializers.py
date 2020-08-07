from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util

#We import force_str in order to retreive the human readable id
class RegisterSerializer(serializers.ModelSerializer):#Added Registeration Serializer, with conditions
    password = serializers.CharField(
        max_length=255, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password'
                  ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError('This username should only contain alphanumeric characters')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EmailVerificationSerializer(serializers.ModelSerializer): #Email Verification Serializer
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']

class LoginSerializer(serializers.ModelSerializer):# Created Login Serializer Linking refresh tokens from jwt
    email = serializers.EmailField(
        max_length=255, min_length=8)
    password = serializers.CharField(
        max_length=68, min_length=3, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)
    tokens = serializers.CharField(
        max_length=68, min_length=3,read_only=True)

    class Meta:
        model=User
        fields=['email','password','username','tokens']


    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        
        user = auth.authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account Disabled, contact Admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not Verified')
        

        return{
            'email':user.email,
            'username':user.username,
            'tokens':user.tokens
        }
        return super().validate(attrs)


class ResetPasswordRequestEmailSerializer(serializers.ModelSerializer): #Email Verification Serializer
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=8)
    class Meta:
        fields = ['email']
                
class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)
    token = serializers.CharField(
        min_length=1,write_only=True)

    class Meta:
        fields = ['password','token','uidb64']
    
    def validate(self,attrs):
        try:
            password=attrs.get('password')
            uidb64=attrs.get('uidb64')
            token=attrs.get('token')

            id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is Invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is Invalid', 401)
        