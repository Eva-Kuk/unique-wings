from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Review


@receiver(post_save, sender=Review)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update a product's average rating when update/create
    """
    instance.product.calculate_rating()


@receiver(post_delete, sender=Review)
def update_on_delete(sender, instance, **kwargs):
    """
    Update a product's average rating when delete
    """
    if instance.product:
        instance.product.calculate_rating()
