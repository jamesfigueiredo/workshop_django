from django.db import models
from products.models import Product


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='sale_product')
    quantity = models.IntegerField()
    descrition = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product) # caso seja nulo, não devolverár erro.