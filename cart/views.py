from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from menu.models import Product


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Adding items in the shopping cart
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    """
    If a product already exist in the cart, update the quantity.
    If a product is not inside the cart, add it with the quantity.
    """
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request,
            (
                f'Updated {product.name} quantity to {cart[item_id]}'
            )
        )
    else:
        cart[item_id] = quantity
        messages.success(
            request,
            (
                f'{product.name} has been added to your cart'
            )
        )
    request.session['cart'] = cart

    print(request.session['cart'])
    return redirect(redirect_url)


def update_cart(request, item_id):
    """
    Functionality for the update button in the shopping cart
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # Store the shopping cart in the HTTP session
    cart = request.session.get('cart', {})

    """
    if the updated quantity is greater than zero, update the quantity
    otherwise remove the item from the cart.
    """

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request,
            (
                f'Updated {product.name} quantity to {cart[item_id]}'
            )
        )
    else:
        cart.pop(item_id)
        messages.success(
            request, f'{product.name} has been removed from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    This functionality remove the item from the shopping cart
    with the click of the delete button
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        # Store the shopping cart in the HTTP session
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(
            request,
            (
                f'{product.name} has been removed from your cart'
            )
        )

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
