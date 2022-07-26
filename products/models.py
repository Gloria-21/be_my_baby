from django.db import models
from django.contrib.auth.models import User


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
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """
    Product review model
    """
    class Meta:
        ordering = ['-date_added']

    rating_selection = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    product = models.ForeignKey(
        Product, related_name="reviews",
        null=True, blank=True, on_delete=models.SET_NULL)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=254)
    content = models.TextField(blank=True, null=True)
    rating = models.IntegerField(choices=rating_selection, default=3)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
