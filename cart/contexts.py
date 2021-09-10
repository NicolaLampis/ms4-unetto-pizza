from django.conf import settings


def cart_contents(request):
    """ Makes the cart content available across the entire site """
    cart_items = []
    sub_total = 0
    order_total = 0
    product_count = 0
    delivery_threshold = settings.FREE_DELIVERY_THRESHOLD
    delivery_charge = settings.DELIVERY_CHARGE

    if sub_total < delivery_threshold:
        delivery = delivery_charge
        free_delivery_delta = delivery_threshold - sub_total
    else:
        delivery = 0
        free_delivery_delta = 0

    order_total = delivery + sub_total

    context = {
        'cart_items': cart_items,
        'sub_total': sub_total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'delivery_threshold': delivery_threshold,
        'order_total': order_total,
    }

    return context
