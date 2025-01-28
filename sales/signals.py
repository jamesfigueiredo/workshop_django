from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from sales.models import Sale


@receiver(post_save, sender=Sale)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity  -= instance.quantity
            product.save()