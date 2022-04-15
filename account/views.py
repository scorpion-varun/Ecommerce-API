from multiprocessing import context
from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from account.serializers import UserRegistrationSerializer
from account.serializers import UserLoginSerializer
from account.renderers import UserRenderer
from account.serializers import UserProfileSerializer
from rest_framework import permissions

from account.serializers import UserChangePasswordSerializer
from account.serializers import SendPasswordResetEmailSerializer
from account.serializers import UserPasswordResetSerializer
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration Successful'},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user =authenticate(email=email, password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login Successfull'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors': {'non_field_errors':['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes =[permissions.IsAuthenticated,]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes = [permissions.IsAuthenticated,]
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetemailView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, format=None):
        serializer= SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset link send. Please check your email'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPasswordResetView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, uid, token,format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class LogoutView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes =[permissions.IsAuthenticated,]
    
    def post(self, request):
        print(request.data)
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            print(token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes =[permissions.IsAuthenticated,]

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)