from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import authentication_classes, api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from user_management.models import *
from .models import *


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
@renderer_classes([JSONRenderer])
def Deposit_IPN(request):
    print(request.data)
    # merchant_id = '2f4df706e2d6200f97b1fdb3697f8750'
    # tx_id,address,status,currency,amount,fiat_coin,fiat_amount = request.data.get('txn_id'),request.data.get('address'), int(request.data.get('status')),\
    # request.data.get('currency'),request.data.get('amount'),request.data.get('fiat_coin'),request.data.get('fiat_amount')
    # if request.data.get('merchant') != merchant_id:
    #     return Response('fuck uuuuu hackers')
    # user = Data_User.objects.filter(address=address)
    # value_token = format(float(fiat_amount),'.2f')
    # if status < 100 :
    #     return Response('belom masuk gan')
    # elif status == 100 and Deposit.objects.filter(depo_id=tx_id).exists() == False:
    #     user.update(token=F('token')+value_token )
    #     Deposit.objects.create(user=user.first(), coin=currency,value_deposit=float(fiat_amount),value_coin=float(amount),value_token=value_token,depo_id=tx_id)
    #     return Response('mantab gan')
    return Response('eror nich')
