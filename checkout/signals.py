from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem
"""
A Signal is sent by django to the entire application after a
model instance is saved/deleted
"""


@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    When an orderitem is created/updated, update the order total
    """
    instance.order.update_order_total()


@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """
    When an orderitem is deleted, update the order total
    """
    instance.order.update_order_total()
