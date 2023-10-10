from django.urls import path

from . views import paymentView, paymentGet


urlpatterns = [
    path('paymentView/', paymentView.as_view()),
    path('paymentViewGet/', paymentGet.as_view()),
]