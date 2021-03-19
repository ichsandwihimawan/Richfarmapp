from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.crypto import get_random_string

#THIRD PARTY
from mptt.models import MPTTModel, TreeForeignKey

class Role(models.Model):
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.role
class Data_User(MPTTModel):
    pos = (
        ('0','KANAN'),
        ('1','KIRI')
    )
    referal_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_rel = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role,on_delete=models.SET_NULL,null=True,default=1)
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(max_length=50, null=True,blank=True)
    position = models.CharField(max_length=1,null=True,blank=True,choices=pos)
    referal_code = models.CharField(max_length=6, unique=True, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    balance = models.FloatField(default=0)
    trx_address = models.CharField(max_length=50,null=True,blank=True)
    doge_address = models.CharField(max_length=50,null=True,blank=True)
    bnb_address = models.CharField(max_length=50,null=True,blank=True)
    bnb_memo = models.CharField(max_length=50,null=True,blank=True)
    total_bonus = models.FloatField(null=True,blank=True,default=0)

    def __str__(self):
        return f'{self.user_rel.username}'

class Reset_Password(models.Model):
    user = models.OneToOneField(Data_User, on_delete=models.CASCADE)
    reset_token = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name







