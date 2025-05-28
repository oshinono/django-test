from django.db import models

class CouponUsage(models.TextChoices):
    ONCE = 'once'
    FOREVER = 'forever'
    REPEATING = 'repeating'

class Discount(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.TextField(choices=CouponUsage.choices, default=CouponUsage.ONCE)
    created_at = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.id
    
    