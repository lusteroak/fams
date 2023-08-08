from enum import Enum

class Manufacturers(Enum):
    bitmain = ('Bitmain', 'Bitmain Technologies Ltd.')
    ebang = ('Ebang', 'Ebang International Holdings Inc')
    microbt = ('Microbt', 'MicroBT WhatsMiner')
    
    @classmethod
    def get_value(cls, member):
        return member.value[0]

class ModelsOfMiners(Enum):
    s9 = ('S9', 'Bitmain | S9 | 13.5 TH/s')
    s9i = ('S9i', 'Bitmain | S9i | 13.5 TH/s')

    @classmethod
    def get_value(cls, member):
        return member.value[0]