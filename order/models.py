from itertools import product
from statistics import mode
from django.db import models
from order.enums import Status
from product.models import Customer, Product
from order.utils import create_order_number


class Order(models.Model):
    order_number=models.CharField(max_length = 10, 
            blank=True,
            editable=False,
            unique=True,
        )
    status = models.CharField(max_length=255, choices=Status.choices(),null=False, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        self.order_number = create_order_number()
        return super(Order, self).save( *args, **kwargs)
    
    def __str__(self):
        return self.order_number



 
class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price=models.DecimalField(max_digits=5, decimal_places=2)
    quantity=models.IntegerField()
    shipped_date=models.DateTimeField(auto_now=True, null=True)
    delivered_date=models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return str(self.id)

    