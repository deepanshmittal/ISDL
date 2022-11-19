from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(Bill)
admin.site.register(ItemList)
admin.site.register(Quotation)
admin.site.register(Purchase)
admin.site.register(MainGateEntry)
