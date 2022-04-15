from django.urls import path
from . views import  ListProduct,CreateProduct, UpdateProduct, DeleteProducts, RetrieveProduct
urlpatterns = [
    
    path('products/list', ListProduct.as_view(),),
    path('products/create', CreateProduct.as_view(),),
    path('products/update/<str:pk>', UpdateProduct.as_view(),),
    path('products/retrieve/<str:pk>', RetrieveProduct.as_view(),),
    path('products/delete/<str:pk>', DeleteProducts.as_view(),),
    

]