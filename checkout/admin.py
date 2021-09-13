from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order_item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_sub_total',
                       'order_total',)

    fields = ('order_number', 'date', 'first_name',
              'last_name', 'email', 'phone_number',
              'town_or_city', 'postcode',
              'street_address1', 'street_address2',
              'delivery_cost', 'order_sub_total',
              'order_total',)

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'order_sub_total',
                    'delivery_cost', 'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
