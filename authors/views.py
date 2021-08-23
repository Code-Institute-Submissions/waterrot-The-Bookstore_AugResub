from django.shortcuts import render, get_object_or_404
from products.models import Author, Product
from django.db.models.functions import Lower


# Create your views here.
def all_authors(request):
    """ A view to show all authors """

    authors = Author.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                authors = authors.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            authors = authors.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'authors': authors,
        'current_sorting': current_sorting,
    }

    return render(request, "authors/authors.html", context)


def author_detail(request, author_id):
    """ A view to show individual authors details """

    author = get_object_or_404(Author, pk=author_id)
    products = Product.objects.all().filter(author=author_id)

    context = {
        'author': author,
        'products': products,
    }

    return render(request, 'authors/author_detail.html', context)
