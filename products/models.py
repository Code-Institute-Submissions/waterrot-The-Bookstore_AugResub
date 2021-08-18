from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    has_formats = models.BooleanField(default=False, null=True, blank=True)
    author = models.ForeignKey('Author', null=True, blank=True,
                               on_delete=models.SET_NULL)
    new_release = models.BooleanField(default=False, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=128)
    date_of_birth = models.CharField(max_length=254, null=True, blank=True)
    summary = models.TextField()
    amazon_link = models.URLField(max_length=1024, null=True, blank=True)
    birth_country = models.CharField(max_length=254, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    books = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
