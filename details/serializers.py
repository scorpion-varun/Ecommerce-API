from rest_framework import serializers
from details.models import  Address


# class DetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Details
#         fields='__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields='__all__'