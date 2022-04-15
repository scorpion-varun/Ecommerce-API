from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from cart.serializers import CartSerializer
from cart.models import Cart
from wishlist.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ListCartItems(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsOwnerOrReadOnly,permissions.IsAuthenticated)
    def get(self, request, format=None):
        items = Cart.objects.all().filter(user_id=request.user)
        serializer = CartSerializer(items, many=True)
        return Response(serializer.data)

class CreateCartItems(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsOwnerOrReadOnly,permissions.IsAuthenticated)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DeleteCartItems(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsOwnerOrReadOnly,permissions.IsAuthenticated)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer