from django.shortcuts import (
        render, redirect, reverse)
from .models import Product, Category, Deal
from django.contrib import messages
from django.db.models import Q


def all_products(request):
    """A view to show all products, including sorting and search queries"""
    products = Product.objects.all()
    query = None
    categories = None
    deals = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'deal' in request.GET:
            deals = request.GET['deal'].split(',')
            products = products.filter(deal__name__in=deals)
            deals = Deal.objects.filter(name__in=deals)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any \
                               search criteria!")
                return redirect(reverse('menu'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            products = products.filter(queries)
    context = {
        'products': products,
        'search_term': query,
        'current_category': categories,
        'deals': deals,
    }
    return render(request, 'menu/menu.html', context)
