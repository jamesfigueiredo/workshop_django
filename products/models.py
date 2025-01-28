from django.db import models
from brands.models import Brand
from categories.models import Category
from models.models import Model


class Product(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='brand_product')
    model = models.ForeignKey(Model, on_delete=models.PROTECT, related_name='model_product')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category_product')
    description = models.TextField(blank=True, null=True)
    serie_number = models.CharField(max_length=100, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='products/', blank=True, null=True) # Novo campo para fotos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name