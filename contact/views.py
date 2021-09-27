from django.shortcuts import render


def contact(request):
    """ A view to return the About page """
    return render(request, 'contact/contact.html')
