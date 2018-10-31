from django.contrib import admin
from zappyapp.models import Product,Customer,Order



class ProductAdmin(admin.ModelAdmin):
    list_display=['cat_choice','price','pname']
    list_filter=['cat_choice']
    list_editable=['price','pname']

admin.site.register(Product,ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display=['customer','cust_address','mobile']
    list_filter=['customer']
    list_editable=['mobile']

admin.site.register(Customer,CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=['users','delievery_address','status']
    list_filter=['users','status']
    list_editable=['status']
admin.site.register(Order,OrderAdmin)
# admin.site.register(Cart)
