
from .views import *
from django.urls import path,include


urlpatterns = [

    path('cart' , cart , name="cart"),
        
]