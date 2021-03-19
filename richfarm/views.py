import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user_management.forms import *
from django.utils.crypto import get_random_string
from user_management.coin_payment import *

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'invalid username or passsword')
        return redirect('login')
    return render(request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('login')

def registerView(request):
    API_KEY = 'f194487ef92fa5f956bf7e6325ec99215f746a3e13ddcffeb3efc05c6745dc2c'
    API_SECRET = 'ceD85F90fd4dBE324734167f57F323f978a2134e0dEFebe0aa7b52Fa9Ef8549B'
    IPN_URL = 'https://richfarm.app/transaction/ipn-depo/'
    client = CryptoPayments(API_KEY, API_SECRET, IPN_URL)
    ref_code = request.GET.get('ref_code',None)
    if Data_User.objects.filter(referal_code = ref_code).exists() == False:
        ref_code = None
    form = Register_Form(initial={'referal_code':ref_code})
    if request.method == 'POST':
        form = Register_Form(data=request.POST)
        if form.is_valid():
            new_ref_code = get_random_string(length=6).upper()
            us = User.objects.create_user(username=request.POST.get('username'),
                                          password=request.POST.get('password1'))
            ref_by = Data_User.objects.get(referal_code=request.POST.get('referal_code'))
            def findParent(a):
                par = a
                if par.get_children().filter(position=request.POST.get('position')).exists():
                    par = par.get_children().get(position=request.POST.get('position'))
                    return findParent(par)
                return par
            parent = findParent(ref_by)
            coin = ['DOGE', 'TRX', 'BNB']
            addr_doge = ''
            addr_trx = ''
            addr_bnb = ''
            memo_bnb = ''
            for x in coin:
                if x == 'BNB':
                    post_params = {
                        'currency': x,
                        'label': request.POST.get('username'),
                        'ipn_url': IPN_URL
                    }
                    address = client.getCallbackAddress(post_params)
                    addr_bnb = json.loads(address.decode('utf-8'))['result']['address']
                    memo_bnb = json.loads(address.decode('utf-8'))['result']['dest_tag']
                elif x == 'DOGE':
                    post_params = {
                        'currency': x,
                        'label': request.POST.get('username'),
                        'ipn_url': IPN_URL
                    }
                    address = client.getCallbackAddress(post_params)
                    addr_doge = json.loads(address.decode('utf-8'))['result']['address']
                elif x == 'TRX':
                    post_params = {
                        'currency': x,
                        'label': request.POST.get('username'),
                        'ipn_url': IPN_URL
                    }
                    address = client.getCallbackAddress(post_params)
                    addr_trx = json.loads(address.decode('utf-8'))['result']['address']

            new_user = Data_User.objects.create(user_rel=us,
                                     parent=parent,
                                     referal_by=ref_by,
                                     name=request.POST.get('name'),
                                     email=request.POST.get('email'),
                                     position=request.POST.get('position'),
                                     referal_code = new_ref_code,
                                     trx_address=addr_trx,
                                     doge_address=addr_doge,
                                     bnb_address=addr_bnb,
                                     bnb_memo=memo_bnb,
                                     )
            messages.success(request,"Registration Successfully, Please login")
            return redirect('login')
    context = {
        'form':form,
        'ref_code':ref_code
    }
    return render(request,'register.html',context)