# Generated by Django 3.1.7 on 2021-03-18 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0004_auto_20210318_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_user',
            old_name='bonus_pairing',
            new_name='total_bonus',
        ),
        migrations.RemoveField(
            model_name='data_user',
            name='bonus_roi',
        ),
        migrations.RemoveField(
            model_name='data_user',
            name='bonus_sponsor',
        ),
    ]
