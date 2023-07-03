from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(CountyCustomer)
admin.site.register(Enterprise)
admin.site.register(Service)
admin.site.register(Defaulter)
admin.site.register(Revenue)
admin.site.register(Invoice)
admin.site.register(MpesaResponse)