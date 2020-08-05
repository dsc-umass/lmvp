from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

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

    