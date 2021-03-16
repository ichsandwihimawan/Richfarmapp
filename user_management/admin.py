from django.contrib import admin
from .models import *

#THIRD PARTY
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
admin.site.register(Data_User)
admin.site.register(Reset_Password)

