from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order_item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_sub_total',
                       'order_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'date', 'first_name',
              'last_name', 'email', 'telephone',
              'town_or_city', 'postcode',
              'address_line1', 'address_line2',
              'delivery_cost', 'order_sub_total',
              'order_total', 'original_cart',
              'stripe_pid')

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'order_sub_total',
                    'delivery_cost', 'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
