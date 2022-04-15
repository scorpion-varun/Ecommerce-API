
from django.db import models


from account.models import User
import uuid

# Create your models here.




class Address(models.Model):
    address_id =  models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone= models.IntegerField()
    house_no=models.CharField(max_length=500)
    landmark=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    country=models.CharField(max_length=100)
    pincode =models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

# class Details(models.Models):
#     details_id= models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     customer_id = models.OneToOneField(User, on_delete=models.CASCADE)
#     addresses = models.ForeignKey(Address, on_delete=models.CASCADE)