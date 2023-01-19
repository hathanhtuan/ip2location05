from django.contrib import admin

from ip2location05app.models.AccessGroup import AccessGroup
from ip2location05app.models.AccessRecord import AccessRecord
from ip2location05app.models.Api3rdParty import Api3rdParty
from ip2location05app.models.ApiConfiguration import ApiConfiguration
from ip2location05app.models.Config import Config
from ip2location05app.models.FileInput import FileInput
from ip2location05app.models.IPAddress import IPAddress
from ip2location05app.models.IPNetwork import IPNetwork
from ip2location05app.models.ISP import ISP
from ip2location05app.models.Result import Result

# Register your models here.


class IPNetworkAdmin(admin.ModelAdmin):
    ordering = ['isp']
    list_display = ('ip_network', 'isp')


admin.site.register(Config)
admin.site.register(IPAddress)
admin.site.register(FileInput)
admin.site.register(Result)
admin.site.register(Api3rdParty)
admin.site.register(ApiConfiguration)
admin.site.register(ISP)
admin.site.register(IPNetwork, IPNetworkAdmin)
admin.site.register(AccessGroup)
admin.site.register(AccessRecord)
