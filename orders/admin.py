from django.contrib import admin
from django.core.urlresolvers import reverse

from .models import Order, OrderItem


def order_detail(obj):
    return '<a href="{}">View</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id])
    )

order_detail.allow_tags = True


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    '''
        Admin View for Order
    '''
    list_display = ('id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', order_detail)
    list_filter = ('paid', 'created', 'updated')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
