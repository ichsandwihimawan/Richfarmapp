from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('',login_required(dashboardView,login_url='login'),name='dashboard'),
    path('profile/',login_required(profileView,login_url='login'),name='profile'),
    path('tree/<str:user_id>/',login_required(treeView,login_url='login'),name='tree'),
    path('register/tree/',login_required(registerTree,login_url='login'),name='register-tree'),
]
