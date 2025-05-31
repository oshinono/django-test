import uuid
from django.http import JsonResponse
from payments.schemas import PaymentOut
from payments.service import PaymentService
from loguru import logger

def create_payment_session(request, order_id: uuid.UUID):
    currency = request.GET.get('currency')
    session_id = PaymentService.create(order_id, currency)
    return JsonResponse(PaymentOut(session_id=session_id).model_dump())
