from django.core.management.base import BaseCommand
from django.db.models import F, Sum
from django.utils import timezone
from transaction.models import *


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        all_user = Data_User.objects.all()
        for x in all_user:
            if x.get_children().filter(position=1).exists() and x.get_children().filter(
                    position=0).exists() and x.get_children().count() == 2:
                anak_kanan = x.get_children().get(position=0).get_descendants(include_self=True).filter(
                    role__role='user')
                anak_kiri = x.get_children().get(position=1).get_descendants(include_self=True).filter(
                    role__role='user')
                omset_kanan = \
                    Invest.objects.filter(user__in=anak_kanan, created_at__date=timezone.now().date()).aggregate(
                        Sum('nominal'))[
                        'nominal__sum'] if Invest.objects.filter(user__in=anak_kanan,
                                                                 created_at__date=timezone.now().date()).exists() else 0

                omset_kiri = \
                    Invest.objects.filter(user__in=anak_kiri, created_at__date=timezone.now().date()).aggregate(
                        Sum('nominal'))[
                        'nominal__sum'] if Invest.objects.filter(user__in=anak_kiri,
                                                                 created_at__date=timezone.now().date()).exists() else 0
                invest_user = Invest.objects.filter(user=x,is_active=True)
                bon_pairing = ((float(omset_kanan) + float(omset_kiri)) / 2) * 0.1 if float(omset_kanan) and float(omset_kiri) != 0 else 0
                if invest_user.exists():
                    if invest_user.first().capping - bon_pairing > 0 and bon_pairing > 0:
                        Bonus_Pairing.objects.create(user=x,nominal=bon_pairing,omset_kiri=omset_kiri,omset_kanan=omset_kanan)
                        user =Data_User.objects.filter(id=x.id)
                        user.update(total_bonus=F('total_bonus')+bon_pairing)
                        invest_user.update(capping=F('capping')-bon_pairing)
                        print(f'generate bonus pairing {x}', bon_pairing)
                    elif invest_user.first().capping - bon_pairing <= 0 and bon_pairing > 0:
                        new_bonus_pairing = invest_user.first().capping
                        Bonus_Pairing.objects.create(user=x, nominal=new_bonus_pairing,omset_kiri=omset_kiri,omset_kanan=omset_kanan)
                        user = Data_User.objects.filter(id=x.id)
                        user.update(total_bonus=F('total_bonus') + new_bonus_pairing)
                        invest_user.update(capping=0,is_active=False)
                        print(f'generate bonus pairing {x}', new_bonus_pairing)
                else:

                    print(x,': no bonus pairing')





