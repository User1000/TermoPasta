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


class AdminItem(admin.ModelAdmin):
    list_filter = ("category",)
    list_display = ("name", "category", "price","order_index")

admin.site.register(Category)
admin.site.register(Item, AdminItem)
admin.site.register(Order, AdminOrder)
# admin.site.register(OrderItem)
admin.site.register(Client)