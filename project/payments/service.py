import uuid
import stripe
from django.shortcuts import get_object_or_404
from orders.models import Order
from config import settings


class PaymentService:

    @classmethod
    def create(cls, order_id: uuid.UUID):
        order = get_object_or_404(Order, id=order_id)

        success_url = f'http://localhost:8000/orders'
        cancel_url = f'http://localhost:8000/order/{order_id}'

        session_create_info = {
            'mode': 'payment',
            'success_url': success_url,
            'cancel_url': cancel_url,
            'payment_method_types': ['card'],
            'line_items': [],
            'discounts': [{'coupon': coupon.id} for coupon in order.discounts.all()]
        }
        for item in order.items.all():
            session_create_info['line_items'].append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
                'tax_rates': [tax.id for tax in order.taxes.all()]
            })

        session = stripe.checkout.Session.create(
            api_key=settings.stripe_secret_key,
            **session_create_info
        )

        return session.id
    
