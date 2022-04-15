from django.urls import path
from wishlist.views import  ListWishlistItem, CreateWishlistItem,  UpdateWishlistItem, DeleteWishlistItem
urlpatterns = [
    
    path('wishlist/list', ListWishlistItem.as_view(),),
    path('wishlist/create', CreateWishlistItem.as_view(),),
    path('wishlist/update/<str:pk>', UpdateWishlistItem.as_view(),),
    path('wishlist/delete/<str:pk>', DeleteWishlistItem.as_view(),),
    

]