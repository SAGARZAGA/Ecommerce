from . import views
from django.urls import path
app_name= 'Search_app'

urlpatterns = [
    path('',views.SearchResult,name= 'SearchResult'),
]