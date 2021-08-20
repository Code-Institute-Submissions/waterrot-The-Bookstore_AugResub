from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Author
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .forms import ProductForm


# Create your views here.
def all_authors(request):
    """ A view to show all authors """

    
    return render(request, "authors/authors.html", context)


def author_detail(request, author_id):
    """ A view to show individual authors details """

    author = get_object_or_404(Author, pk=author_id)

    context = {
        'author': author,
    }

    return render(request, 'author/author_detail.html', context)


@login_required
def add_author(request):
    """ Add an author to the store """
    
    return render(request, template, context)


@login_required
def edit_author(request, product_id):
    """ Edit an author in the store """
    
    return render(request, template, context)


@login_required
def delete_author(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    messages.success(request, 'Author deleted!')
    return redirect(reverse('author'))
