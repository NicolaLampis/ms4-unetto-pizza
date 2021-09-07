from django.db import models


# Category
class Category(models.Model):
    """ Model for category instances """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_frinendly_name(self):
        return self.friendly_name


# Product
class Product(models.Model):
    """ Model for product instances """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    favourite = models.BooleanField(default=False)
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    deal = models.ForeignKey(
        'Deal',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    allergens = models.ManyToManyField('Allergen')

    def __str__(self):
        return self.name


# Deal
class Deal(models.Model):
    """
    Deals Model is for special offer, allows the grouping of
    products for easier searches
    """
    name = models.CharField(
        max_length=254)
    friendly_name = models.CharField(
        max_length=254)

    def __str__(self):
        return self.name

    def get_deal_friendly_name(self):
        return self.friendly_name


# Allergen
class Allergen(models.Model):
    """
    Allergen is used to inform consumers of the presence of
    allergen in the food
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    data_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_allergen_friendly_name(self):
        return self.friendly_name
