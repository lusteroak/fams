import importlib

from django.db import models
from django.utils import timezone


class HostingUser(models.Model):    
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    number_of_miners = models.CharField(max_length=50)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.lastname}'

    
    
