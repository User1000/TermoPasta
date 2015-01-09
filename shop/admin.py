from django.contrib import admin
from models import *
# Register your models here.

class InlineOrderItem(admin.StackedInline):
    model = OrderItem
    extra = 0

class AdminOrder(admin.ModelAdmin):
    readonly_fields = ['date', 'order_items']
    list_display = ['client', 'date', 'order_items']
    inlines = [InlineOrderItem, ]



admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order, AdminOrder)
# admin.site.register(OrderItem)
admin.site.register(Client)