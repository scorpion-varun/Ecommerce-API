from signal import raise_signal
import uuid
from django.shortcuts import render
from rest_framework import status
from api.models import Category, Products
from . serializers import CategorySerializer, ProductsSerializer
from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
import uuid
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters import rest_framework as filters
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.filters import OrderingFilter, SearchFilter

# Create your views here.
# class RegistrationAPIView(generics.GenericAPIView):
#     serializer_class = RegistrationSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data = request.data)
#         # serializer.is_valid(raise_exception = True)
#         # serializer.save()
#         if (serializer.is_valid()):
#             serializer.save()
#             return Response({
#                 "RequestId":str(uuid.uuid4()),
#                 "Message": "user Created Succesfully",
#                 "user":serializer.data})
#         return Response({"Errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# class LogoutAPIView(generics.GenericAPIView):
#    permission_classes = (permissions.IsAuthenticated,)

#    def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

        

### API For Listing Products #####

class ListProduct(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ()
    search_fields = ('title')

class CreateProduct(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAdminUser,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class RetrieveProduct(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class UpdateProduct(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAdminUser,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class DeleteProducts(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAdminUser,)
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer