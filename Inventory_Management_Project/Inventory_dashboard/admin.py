from django.contrib import admin

from .models import Product

from .models import Order
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity','expirydate',)
    list_filter=['category']
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.site_header='Sr Inventory Dashboard'