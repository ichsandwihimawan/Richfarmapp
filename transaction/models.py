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

    def __str__(self):
        return "{} {}".format(self.user, self.value_deposit)