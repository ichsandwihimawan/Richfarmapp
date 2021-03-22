from django.core.management.base import BaseCommand
from django.db.models import F
from transaction.models import *
class Command(BaseCommand):
    help = 'generate_roi'

    def handle(self, *args, **kwargs):
        all_invest =  Invest.objects.filter(is_active=True,user__role__role='user')
        roi = Roi_Percentage.objects.first().persenan / 100
        print(all_invest)
        print(roi,'roinya')
        for x in all_invest:
            bonus = x.nominal * roi
            print(bonus)
            print(x.capping - bonus)
            if x.capping - bonus > 0 :
                Bonus_Roi.objects.create(user_invest=x,roi=bonus)
                inv =Invest.objects.filter(id=x.id)
                user = Data_User.objects.filter(id=x.user.id)
                inv.update(capping=F('capping')-bonus,current_roi=F('current_roi')+bonus)
                user.update(total_bonus=F('total_bonus')+bonus)
                print(f'generating roi for {x.user} : {bonus}')
            else:
                inv = Invest.objects.filter(id=x.id)
                user = Data_User.objects.filter(id=x.user.id)
                inv.update(capping=0,is_active=False,current_roi=F('current_roi')+bonus)
                new_bonus = x.capping
                Bonus_Roi.objects.create(user_invest=x, roi=new_bonus)
                user.update(total_bonus=F('total_bonus') + new_bonus)
                print(f'generating roi for {x.user} : {new_bonus}')



