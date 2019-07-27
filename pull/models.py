from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class PolycomIpPhone(models.Model):
    phone_ip = models.GenericIPAddressField()
    mac_address = models.CharField(max_length = 20)
    time_stamp = models.DateTimeField(null = True)

class On_Off_hook(PolycomIpPhone):
    #phone = models.ForeignKey(PolycomIpPhone, on_delete = models.CASCADE)
    line_num = models.IntegerField(null= True)
    status = models.CharField(max_length = 20)

class Call_details(PolycomIpPhone):
    #phone = models.ForeignKey(PolycomIpPhone, on_delete = models.CASCADE)
    call_reference = models.CharField(max_length = 10)
    call_state = models.CharField(max_length = 10)
    call_type = models.CharField(max_length = 20)
    UI_Appearance_Index = models.CharField(max_length = 5)
    called_party_name = models.CharField(max_length = 20, null = True)
    called_party_dir_num = models.TextField(null = True)
    calling_party_name = models.CharField(max_length = 20)
    calling_party_dir_num = models.TextField(null= True)
    call_duration = models.CharField(max_length = 10 ,null= True)
    protocol = models.CharField(max_length = 10)
    muted = models.IntegerField(null= True)
    ringing = models.IntegerField(null= True)
    





#print(help(On_Off_hook))
