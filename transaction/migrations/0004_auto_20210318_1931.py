# Generated by Django 3.1.7 on 2021-03-18 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0005_auto_20210318_1931'),
        ('transaction', '0003_auto_20210318_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='invest',
            name='capping',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Bonus_Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominal', models.FloatField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_invest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.invest')),
            ],
        ),
        migrations.CreateModel(
            name='Bonus_Roi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roi', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_invest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.invest')),
            ],
        ),
        migrations.CreateModel(
            name='Bonus_Pairing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominal', models.FloatField(blank=True, default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.data_user')),
            ],
        ),
    ]