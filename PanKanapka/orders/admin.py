from django.contrib import admin
from .models import Order, OrderSandwiches

class OrderAdmin(admin.ModelAdmin):

    list_display = ('get_username', 'get_company', 'get_sandwiches')
    list_filter = ('user__group__name',)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderSandwiches)