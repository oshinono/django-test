from enum import Enum
from pydantic import BaseModel

class PaymentOut(BaseModel):
    session_id: str
