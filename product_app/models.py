from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    # this is used to view info in Django Admin
    def __str__(self) -> str:
        return self.name




class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    # this is used to view info in Django Admin
    def __str__(self) -> str:
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    # by on_delete: CASCADE if we delete brand all the products will deleted and vice versa is not true
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )

    # this is used to view info in Django Admin
    def __str__(self) -> str:
        return self.name



