# Generated by Django 3.1.7 on 2021-03-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_auto_20210318_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_user',
            name='bnb_memo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
