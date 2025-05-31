import uuid
from django.db import models

class Currency(models.TextChoices):
    USD = 'USD'
    RUB = 'RUB'

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(default=Currency.RUB, choices=Currency.choices)

    def __str__(self):
        return self.name