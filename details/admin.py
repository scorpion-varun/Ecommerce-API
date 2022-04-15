from ast import Add
from django.contrib import admin

# Register your models here.
from details.models import Address

admin.site.register(Address)