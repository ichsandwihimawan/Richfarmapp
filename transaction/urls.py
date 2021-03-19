from django.urls import path
from .views import *

urlpatterns = [
    path('ipn-depo/',Deposit_IPN,name='deposit-ipn'),
    path('invest/',investView,name='invest')
]