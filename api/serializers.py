


# from lib2to3.pgen2.tokenize import TokenError
# from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from . models import Products, Category
from drf_extra_fields.fields import HybridImageField
# from django.contrib.auth.models import User
# import uuid
# from rest_framework_simplejwt.tokens import RefreshToken, TokenError

# class RegistrationSerializer(serializers.ModelSerializer):
#     user_id = serializers.UUIDField(default=uuid.uuid4)
#     username = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     password= serializers.CharField(max_length=150, write_only=True)
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email','username', 'password', 'user_id')

#     def validate(self, args):
#         email= args.get('email', None)
#         username = args.get('username', None)
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({'email' : {'Email already exists'}})
#         if User.objects.filter(username=username).exists():
#             raise serializers.ValidationError({'username' : {'Username already exists'}})
#         return super().validate(args)

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)


# class LogoutSerializer(serializers.Serializer):
#     refresh = serializers.CharField()
#     default_error_message = {
#         'bad_token':'Token Is Expired Or Invalid'
#     }

#     def validate(self, attrs):
#         self.token= attrs['refresh']
#         return attrs
    
#     def save(self, **kwargs):
#         try:
#             RefreshToken(self.token).blacklist()
#         except TokenError:
#             self.fail('bad_token')




class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    product_image = HybridImageField()
    class Meta:
        model = Products
        fields = '__all__'

