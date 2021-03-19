from django.db import models
from user_management.models import *

# Create your models here.

class Deposit(models.Model):
    user = models.ForeignKey(Data_User, on_delete=models.CASCADE)
    coin = models.CharField(max_length=10,null=True,blank=True)
    value_coin = models.FloatField(null=True,blank=True)
    value_usd = models.FloatField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    depo_id = models.CharField(max_length=100, null=True,blank=True)
    txn_id = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return "{} {}".format(self.user, self.value_usd)

class Invest(models.Model):
    user = models.ForeignKey(Data_User,on_delete=models.CASCADE)
    nominal = models.FloatField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    current_roi = models.FloatField(null=True,blank=True,default=0)
    capping = models.FloatField(null=True,blank=True,default=0)

    def __str__(self):
        return f'{self.user} {self.nominal} {"AKTIF" if self.is_active==True else "NONAKTIF"}'

class Bonus_Sponsor(models.Model):
    for_user = models.ForeignKey(Data_User,on_delete=models.CASCADE)
    user_invest= models.ForeignKey(Invest,on_delete=models.CASCADE)
    nominal = models.FloatField(default=0,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_invest.user} { self.nominal}'

class Bonus_Pairing(models.Model):
    user = models.ForeignKey(Data_User,on_delete=models.CASCADE)
    nominal = models.FloatField(default=0,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.nominal}'

class Bonus_Roi(models.Model):
    user_invest = models.ForeignKey(Invest,on_delete=models.CASCADE)
    roi = models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)















