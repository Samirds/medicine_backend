from django.urls import path

from . views import order_View, order_View_Get


urlpatterns = [
    path('orderView/', order_View.as_view()),
    path('orderViewGet/', order_View_Get.as_view()),
]