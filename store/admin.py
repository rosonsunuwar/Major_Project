from django.contrib import admin
from store.models import *
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Customer)
admin.site.register(Product)
# admin.site.register(Kurtha)
# admin.site.register(Saree)
# admin.site.register(Tshirt)
# admin.site.register(Pant)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
