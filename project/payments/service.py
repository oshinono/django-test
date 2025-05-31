from collections import Counter
import uuid
import stripe
from django.shortcuts import get_object_or_404
from orders.models import Order
from config import settings


class PaymentService:

    @classmethod
    def create(cls, order_id: uuid.UUID, currency: str):
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
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
                'tax_rates': [tax.id for tax in order.taxes.all()]
            })

        # непонятно по какому алгоритму именно выбирать stripe-аккаунт, поэтому пока так
        if currency == 'USD':
            secret_key = settings.stripe_usd_secret_key
        elif currency == 'RUB':
            secret_key = settings.stripe_rub_secret_key
        else:
            raise ValueError(f'{currency} не поддерживается')

        session = stripe.checkout.Session.create(
            api_key=secret_key,
            **session_create_info
        )

        return session.id
    
