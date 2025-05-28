from django.urls import path
from .views import create_payment_session

urlpatterns = [
    path('buy/<uuid:order_id>', create_payment_session, name='buy'),
]