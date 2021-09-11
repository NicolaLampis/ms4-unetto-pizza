from django.conf import settings
from menu.models import Product
from django.shortcuts import get_object_or_404
from decimal import Decimal


def cart_contents(request):
    """ Makes the cart content available across the entire site """
    cart_items = []
    total = 0
    order_total = 0
    product_count = 0
    delivery_threshold = settings.FREE_DELIVERY_THRESHOLD
    delivery_charge = settings.DELIVERY_CHARGE
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < delivery_threshold:
        delivery = delivery_charge
        free_delivery_delta = Decimal(delivery_threshold) - Decimal(total)
    else:
        delivery = 0
        free_delivery_delta = 0

    order_total = Decimal(delivery) + Decimal(total)

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'delivery_threshold': delivery_threshold,
        'order_total': order_total,
    }

    return context
