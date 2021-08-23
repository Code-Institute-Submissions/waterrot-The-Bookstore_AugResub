from django.shortcuts import render, get_object_or_404
from products.models import Product


# Create your views here.
def index(request):
    """ A view to return the index page """

    new_release_1 = get_object_or_404(Product, pk=25)
    new_release_2 = get_object_or_404(Product, pk=83)
    new_release_3 = get_object_or_404(Product, pk=99)

    context = {
        'new_release_1': new_release_1,
        'new_release_2': new_release_2,
        'new_release_3': new_release_3,
    }

    return render(request, "home/index.html", context)
