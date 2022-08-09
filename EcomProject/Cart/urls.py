
from django.urls import path

from Cart import views

app_name= 'Cart'

urlpatterns = [
    path('',views.cart_detail, name='cart_detail') ,
    path('add/<int:product_id>/',views.add_cart, name= 'add_cart') ,
    path('remove/<int:product_id>/',views.cart_remove, name= 'cart_remove') ,
    path('delete/<int:product_id>/',views.cart_delete, name= 'cart_delete') ,
]