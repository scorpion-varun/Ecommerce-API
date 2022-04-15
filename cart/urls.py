from django.urls import path
from cart.views import ListCartItems, CreateCartItems, DeleteCartItems
urlpatterns = [
    
    path('cart/list', ListCartItems.as_view(),),
    path('cart/create', CreateCartItems.as_view(),),
    path('cart/delete/<str:pk>', DeleteCartItems.as_view(),),
    

]