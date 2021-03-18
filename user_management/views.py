import re
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *

def dashboardView(request):

    return render(request,'dashboard/index.html')

def profileView(request):

    return render(request, 'dashboard/profile.html')

def generateJaringan(user,path):
    dt = {}
    node0 = f'<a href="#" ><h1 style="font-size: 20px;"><strong>{user}</strong></h1></a>'
    node1 = user.get_children().get(position='1') if user.get_children().filter(
        position='1').exists() else "Register Here"
    node2 = user.get_children().get(position='0') if user.get_children().filter(
        position='0').exists() else "Register Here"
    wrapnode1 = f'<a href="{path+str(node1.id)+"/"}" ><h1 style="font-size: 20px;"><strong>{node1}</strong></h1></a>' if node1 != 'Register Here' else ''
    wrapnode2 = f'<a href="{path+str(node2.id)+"/"}" ><h1 style="font-size: 20px;"><strong>{node2}</strong></h1></a>'if node2 != 'Register Here' else ''
    node3 = ''
    node4 = ''
    node5 = ''
    node6 = ''

    if node1 == "Register Here":
        wrapnode1 = f'<a href="#" class="node" data-position="1" data-parent="{user.id}" ><h1 style="font-size: 20px; color:red"><strong>Register Here</strong></h1></a>'

    if node2 == "Register Here":
        wrapnode2 = f'<a href="#" class="node" data-position="0" data-parent="{user.id}" ><h1 style="font-size: 20px; color:red;"><strong>Register Here</strong></h1></a>'

    if type(node1)!= str and node1.get_children().filter(position='1').exists():
        node3 = node1.get_children().get(position='1')
        node3 = f'<a href="{path+str(node3.id)+"/"}" ><h1 style="font-size: 20px;"><strong>{node3}</strong></h1></a>'
    elif type(node1) == str:
        node3 = f'<a href="#"><h1 style="font-size: 20px;"><strong>Empty</strong></h1></a>'
    else:
        node3 = f'<a href="#" class="node" data-parent="{node1.id}" data-position="1"><h1 style="font-size: 20px; color:red;"><strong>Register Here</strong></h1></a>'

    if type(node1)!= str and node1.get_children().filter(position='0').exists():
        node4 = node1.get_children().get(position='0')
        node4 = f'<a href="{path+str(node4.id)+"/"}" ><h1 style="font-size: 20px;"><strong>{node4}</strong></h1></a>'
    elif type(node1) == str:
        node4 = f'<a href="#"><h1 style="font-size: 20px;"><strong>Empty</strong></h1></a>'
    else:
        node4 = f'<a href="#" class="node" data-parent="{node1.id}" data-position="0"><h1 style="font-size: 20px; color:red;"><strong>Register Here</strong></h1></a>'

    if type(node2)!= str and node2.get_children().filter(position='1').exists():
        node5 = node2.get_children().get(position='1')
        node5 = f'<a href="{path+str(node5.id)+"/"}"><h1 style="font-size: 20px;"><strong>{node5}</strong></h1></a>'
    elif type(node2) == str:
        node5 = f'<a href="#"><h1 style="font-size: 20px;"><strong>Empty</strong></h1></a>'
    else :
        node5 = f'<a href="#" class="node" data-parent="{node2.id}" data-position="1" ><h1 style="font-size: 20px; color:red"><strong>Register Here</strong></h1></a>'

    if type(node2)!= str and node2.get_children().filter(position='0').exists():
        node6 = node2.get_children().get(position='0')
        node6 = f'<a href="{path+str(node6.id)+"/"}"><h1 style="font-size: 20px;"><strong>{node6}</strong></h1></a>'
    elif type(node2) == str:
        node6 = f'<a href="#"><h1 style="font-size: 20px;"><strong>Empty</strong></h1></a>'
    else :
        node6 = f'<a href="#" class="node" data-parent="{node2.id}" data-position="0"><h1 style="font-size: 20px; color:red"><strong>Register Here</strong></h1></a>'

    if node1 == "Register Here":
        wrapnode1 = f'<a href="#" class="node" data-position="1" data-parent="{user.id}" ><h1 style="font-size: 20px; color:red"><strong>Register Here</strong></h1></a>'
        node3 = f'<a href="#"><h1 style="font-size: 20px;"><strong>Empty</strong></h1></a>'
        node4 = f'<a href="#"><h1 style="font-size: 20px;"><strong>Empty</strong></h1></a>'
    if node2 == "Register Here":
        wrapnode2 = f'<a href="#" class="node" data-position="0" data-parent="{user.id}" ><h1 style="font-size: 20px; color:red;"><strong>Register Here</strong></h1></a>'
        node5 = f'<a href="#"><h1 style="font-size: 20px;"><strong>Empty</strong></h1></a>'
        node6 = f'<a href="#"><h1 style="font-size: 20px;"><strong>Empty</strong></h1></a>'


    dt['node0'] = node0
    dt['node1'] = wrapnode1
    dt['node2'] = wrapnode2
    dt['node3'] = node3
    dt['node4'] = node4
    dt['node5'] = node5
    dt['node6'] = node6
    return dt

def treeView(request,user_id):
    user = Data_User.objects.get(id=user_id)
    path = request.build_absolute_uri(f"/dashboard/tree/")
    tree = generateJaringan(user,path)

    context = {
        'tree':tree,
        'self':request.user.data_user.id,
        '1level':user.parent.id if user.parent != None else request.user.data_user.id,
    }
    return render(request, 'dashboard/tree.html',context)

@api_view(['POST'])
def registerTree(request):
    ref_by = request.user.data_user
    parent = Data_User.objects.get(id=request.data.get('parent_id'))

    if User.objects.filter(username__iexact=request.data.get('username')).exists():
        return Response("Username sudah digunakan",status=status.HTTP_400_BAD_REQUEST)
    if Data_User.objects.filter(email__iexact=request.data.get('email')).exists():
        return Response("Email sudah digunakan",status=status.HTTP_400_BAD_REQUEST)
    if re.search('[A-Z]', request.data.get('password1')) == None \
            or re.search('[0-9]', request.data.get('password1')) == None \
            or re.search('[^A-Za-z0-9]', request.data.get('password1')) == None or len(request.data.get('password1')) < 8:
        return Response("Password Harus mengandung 1 Huruf Besar, 1 Angka, dan 1 Symbol. Minimal 8 Karakter",status=status.HTTP_400_BAD_REQUEST)
    if request.data.get('password1') != request.data.get('password2'):
        return Response('Pasword Tidak Sesuai', status=status.HTTP_400_BAD_REQUEST)
    if parent.get_children().filter(position=request.data.get('position')).exists():
        return Response("Posisi Telah Di isi orang lain, Silahkan refresh ulang halaman anda",status=status.HTTP_400_BAD_REQUEST)

    new_ref_code = get_random_string(length=6).upper()
    us = User.objects.create_user(username=request.data.get('username'),
                                  password=request.data.get('password1'))

    new_user = Data_User.objects.create(user_rel=us,
                                        parent=parent,
                                        referal_by=ref_by,
                                        name=request.data.get('name'),
                                        email=request.data.get('email'),
                                        position=request.data.get('position'),
                                        referal_code=new_ref_code,
                                        )
    return Response("User Berhasil Dibuat")

