# Generated by Django 4.2.4 on 2023-08-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miner',
            name='mining_power',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]