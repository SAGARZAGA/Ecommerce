from . import views
from django.urls import path
app_name= 'EcomApp'

urlpatterns = [
    path('',views.AllProductCat,name= 'AllProductCat'),
    path('<slug:c_slug>', views.AllProductCat, name= 'product_by_category') ,
    path('<slug:c_slug>/<slug:product_slug>/', views.productDetails, name= 'productDetails') ,
    path('buy/', views.buy, name= 'buy') ,
]
