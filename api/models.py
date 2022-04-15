
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.
def upload_to(instance, filename):
    return 'product_images/{filename}'.format(filename=filename)

class Category(models.Model):
    category_id= models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    category_name = models.CharField(max_length=100)

class Products(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=800)
    price = models.IntegerField()
    product_image = models.ImageField(_("Image"), upload_to=upload_to)
    reviews = models.CharField(max_length=400)
