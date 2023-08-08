# Generated by Django 4.2.4 on 2023-08-07 23:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_miner_mining_power'),
    ]

    operations = [
        migrations.AddField(
            model_name='miner',
            name='name_of_miner',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='miner',
            name='pool_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='miner',
            name='manufacturer',
            field=models.CharField(choices=[('Bitmain', 'Bitmain Technologies Ltd.'), ('Ebang', 'Ebang International Holdings Inc'), ('Microbt', 'MicroBT WhatsMiner')], default='Bitmain', max_length=40),
        ),
        migrations.AlterField(
            model_name='miner',
            name='model',
            field=models.CharField(choices=[('S9', 'Bitmain | S9 | 13.5 TH/s'), ('S9i', 'Bitmain | S9i | 13.5 TH/s')], default='S9', max_length=250),
        ),
    ]
