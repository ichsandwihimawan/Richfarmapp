from django.db.models import F, Q
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import authentication_classes, api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from user_management.models import *
from .models import *


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
# @renderer_classes([JSONRenderer])
def Deposit_IPN(request):
    print(request.data)
    merchant_id = '2f4df706e2d6200f97b1fdb3697f8750'
    label = request.data.get('label')
    tx_id = request.data.get('txn_id')
    depo_id = request.data.get('deposit_id')
    status = request.data.get('status')
    currency = request.data.get('currency')
    amount = request.data.get('amount')
    fiat_amount = request.data.get('fiat_amount')
    value_usd = format(float(fiat_amount),'.2f')
    if request.data.get('merchant') != merchant_id:
        return Response('fuck uuuuu hackers')
    user = Data_User.objects.filter(user_rel__username=label)
    if float(status) < 100 :
        return Response('belom masuk gan')
    elif float(status) == 100 and Deposit.objects.filter(depo_id=depo_id).exists() == False:
        user.update(balance=F('balance')+value_usd )
        Deposit.objects.create(user=user.first(),
                               coin=currency,
                               value_coin=float(amount),
                               value_usd=value_usd,
                               depo_id=depo_id,
                               txn_id=tx_id,)
        return Response('mantab gan')
    return Response('eror nich')

@api_view(['POST'])
def investView(request):
    user = request.user.data_user
    nominal = float(request.data.get('paket'))
    if user.balance < nominal:
        return Response("Insuficient Balance, Please Deposit",status=status.HTTP_400_BAD_REQUEST)
    if user.invest_set.filter(is_active=True).exists():
        return Response("You still have Active Invest, Please complete it first", status=status.HTTP_400_BAD_REQUEST)

    inv = Invest.objects.create(user=user,nominal=nominal,capping=nominal*4)
    user.balance -= nominal
    user.save()

    if user.referal_by.invest_set.filter(is_active=True).exists():
        refnya = Data_User.objects.filter(id=user.referal_by.id)
        Bonus_Sponsor.objects.create(user_invest=inv,nominal=nominal*0.1,for_user=refnya.first())
        refnya.update(total_bonus=F('total_bonus')+nominal*0.1,)
        refnya_invest = refnya.first()
        refnya_invest.invest_set.filter(is_active=True).update(capping=F('capping') - nominal * 0.1)

    return Response('Invest Successfully, Please Enjoy your profit')

