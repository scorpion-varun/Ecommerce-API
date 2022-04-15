from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from details.serializers import AddressSerializer
from details.models import Address
from wishlist.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

# Create your views here.


class ListAddress(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsOwnerOrReadOnly,permissions.IsAuthenticated)
    def get(self, request, format=None):
        items = Address.objects.all().filter(user_id=request.user)
        serializer = AddressSerializer(items, many=True)
        return Response(serializer.data)

class CreateAddress(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsOwnerOrReadOnly,permissions.IsAuthenticated)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class UpdateAddress(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication,permissions.IsAuthenticated]
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class DeleteAddress(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsOwnerOrReadOnly,permissions.IsAuthenticated)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer