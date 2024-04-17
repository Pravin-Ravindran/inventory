from django.contrib import admin

from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity','expirydate',)
    list_filter=['category']
admin.site.register(Product,ProductAdmin)
admin.site.site_header='Sr Inventory Dashboard'