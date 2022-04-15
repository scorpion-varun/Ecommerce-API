from django.urls import path
from details.views import  ListAddress, CreateAddress, UpdateAddress, DeleteAddress
urlpatterns = [
    
    path('addresses/list', ListAddress.as_view(),),
    path('addresses/create', CreateAddress.as_view(),),
    path('addresses/update/<str:pk>', UpdateAddress.as_view(),),
    path('addresses/delete/<str:pk>', DeleteAddress.as_view(),),
    

]