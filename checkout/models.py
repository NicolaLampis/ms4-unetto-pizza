from django.db import models
from menu.models import Product
import uuid
from django.conf import settings
from django.db.models import Sum


class Order(models.Model):
    order_number = models.CharField(
        max_length=32,
        null=False,
        editable=False)
    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False)
    last_name = models.CharField(
        max_length=50,
        null=False,
        blank=False)
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False)
    telephone = models.CharField(
        max_length=20,
        null=False,
        blank=False)
    town_or_city = models.CharField(
        max_length=40, null=True,
        blank=False)
    address_line1 = models.CharField(
        max_length=80,
        null=False,
        blank=False)
    address_line2 = models.CharField(
        max_length=80,
        null=True,
        blank=True)
    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=False)
    date = models.DateTimeField(
        auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=5, decimal_places=2,
        null=False, default=0)
    order_sub_total = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=False, default=0)
    order_total = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=False, default=0)

    def _generate_order_number(self):
        """
        Use UUID to generate a unique random order number
        """
        return uuid.uuid4().hex.upper()

    def update_order_total(self):
        """
        Update the order total each time an order-item is
        added and apply relative delivery cost
        """
        self.order_sub_total = self.orderitems.aggregate(
            Sum('order_item_total')
            )['order_item_total__sum'] or 0
        if self.order_sub_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.DELIVERY_CHARGE
        else:
            self.delivery_cost = 0

        self.order_total = self.order_sub_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override save. Set the order number if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE,
        related_name='orderitems')
    product = models.ForeignKey(
        Product, null=False, blank=False,
        on_delete=models.CASCADE)
    quantity = models.IntegerField(
        null=False, blank=False, default=0)
    order_item_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """
        Override save. Set the order item total and update the order total.
        """
        self.order_item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_number}'
