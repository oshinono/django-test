from django.db import models
import uuid

from django.forms import ValidationError
from items.models import Item
from discounts.models import Discount
from taxes.models import Tax

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = models.ManyToManyField(Item, related_name='items')
    taxes = models.ManyToManyField(Tax, blank=True, related_name='taxes')
    discounts = models.ManyToManyField(Discount, blank=True, related_name='discounts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return f"Order {self.id}"

    

    
    
    