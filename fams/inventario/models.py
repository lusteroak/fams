from django.db import models
from django.utils import timezone
from hosting_users.models import HostingUser

from .list_of_miners import Manufacturers, ModelsOfMiners

class Miner(models.Model):
    owner = models.ForeignKey(HostingUser, on_delete=models.CASCADE)
    pool_name = models.CharField(max_length=250)
    name_of_miner = models.CharField(max_length=250)
    manufacturer = models.CharField(max_length=40, choices=[x.value for x in Manufacturers], default=Manufacturers.get_value(Manufacturers.bitmain))
    model = models.CharField(max_length=250, choices=[x.value for x in ModelsOfMiners], default=ModelsOfMiners.get_value(ModelsOfMiners.s9))
    mining_power = models.DecimalField(max_digits=5, decimal_places=1)
    serialInSlot6 = models.CharField(max_length=250)
    serialInSlot7 = models.CharField(max_length=250)
    serialInSlot8 = models.CharField(max_length=250)
    serialPSU = models.CharField(max_length=250)
    maintance_mode = models.BooleanField(default=False)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name_of_miner}'
