

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from api.models import Products
from api.serializers import ProductsSerializer
from account.models import User
from wishlist.models import WishlistItem
from wishlist.serializers import WishlistItemSerializer
from wishlist.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import serializers
from django.shortcuts import get_object_or_404


# Create your views here.
class ListWishlistItem(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsOwnerOrReadOnly,permissions.IsAuthenticated)
    def get(self, request, format=None):
        items = WishlistItem.objects.all().filter(user_id=request.user)
        serializer = WishlistItemSerializer(items, many=True)
        return Response(serializer.data)

class CreateWishlistItem(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsOwnerOrReadOnly,permissions.IsAuthenticated)
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

       
class UpdateWishlistItem(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication,permissions.IsAuthenticated]
    permission_classes = (IsOwnerOrReadOnly)
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

class DeleteWishlistItem(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsOwnerOrReadOnly,permissions.IsAuthenticated)
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer

