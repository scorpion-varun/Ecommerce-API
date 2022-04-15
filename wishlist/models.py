from django.db import models

from account.models import User
from api.models import Products
import uuid

# Create your models here.
class WishlistItem(models.Model):
    wishlist_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)