from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    # we take the order number as an argument and change view and name to checkout_success
]