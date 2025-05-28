import uuid
from django.http import JsonResponse
from payments.schemas import PaymentOut
from payments.service import PaymentService
from loguru import logger

def create_payment_session(request, order_id: uuid.UUID):
    logger.info(order_id)
    session_id = PaymentService.create(order_id)
    return JsonResponse(PaymentOut(session_id=session_id).model_dump())
