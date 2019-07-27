from django.contrib import admin

# Register your models here.
from .models import PolycomIpPhone, On_Off_hook, Call_details

# Register your models here.


class Call_detailsAdmin(admin.ModelAdmin):
    list_display = ('phone_ip', 'mac_address', 'time_stamp', 'call_type', 'called_party_name','calling_party_name','call_duration')
    list_filter = ['phone_ip']
    search_fields = ['calling_party_name']

class PolyComIpPhoneAdmin(admin.ModelAdmin):
    list_display = ('phone_ip', 'mac_address', 'time_stamp')
    

admin.site.register(PolycomIpPhone, PolyComIpPhoneAdmin)
admin.site.register(On_Off_hook) 
admin.site.register(Call_details, Call_detailsAdmin)