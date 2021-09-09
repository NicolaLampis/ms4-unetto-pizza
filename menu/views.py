from django.shortcuts import (
        render, redirect, reverse, get_object_or_404)
from .models import Product, Category, Deal
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower


def all_products(request):
    """A view to show all products, including sorting and search queries"""
    products = Product.objects.all()
    query = None
    categories = None
    deals = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'favourite':
                sortkey = 'favourite'
                sortkey = f'-{sortkey}'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_category': categories,
        'deals': deals,
        'current_sorting': current_sorting,
    }
    return render(request, 'menu/menu.html', context)


def product_detail(request, id):
    """A view to show individual product details"""
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product,
    }
    return render(request, 'menu/product_detail.html', context)
