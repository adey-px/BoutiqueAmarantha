from django.db import models


# Category model
class Category(models.Model):
    """
    Category model based on category.json file.
    """

    # fix spelling issue in admin
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    label = models.CharField(max_length=254, null=True, blank=True)

    # str method, category name
    def __str__(self):
        return self.name

    # str method, category label
    def __str__(self):
        return self.label


# Product model
class Product(models.Model):
    """
    Product model with relevant fields
    """

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # str method, product name
    def __str__(self):
        return self.name
