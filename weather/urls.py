from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'), 
    path('filterdata', views.filter_data, name = 'filterdata'), #the path for our index view
]