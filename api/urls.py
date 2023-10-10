from django.urls import path
from . views import Product_Info_View

urlpatterns = [path("productApi/", Product_Info_View.as_view()),
               ]