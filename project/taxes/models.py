import uuid
from django.db import models

class TaxType(models.TextChoices):
    VAT = 'vat'
    SALES_TAX = 'sales_tax'
    GST = 'gst'

class Tax(models.Model):
    id = models.CharField(primary_key=True)
    type = models.TextField(choices=TaxType.choices, default=TaxType.VAT)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.type
    
    def __repr__(self):
        return f"<Tax(type='{self.type}', rate='{self.rate}')>"
    