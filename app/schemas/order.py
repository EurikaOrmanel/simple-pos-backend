from pydantic import UUID4, BaseModel
from uuid import UUID
from datetime import datetime
from typing import List

from ..schemas.customer import CustomerOutput
from .order_item import OrderItemInput, OrderItemOutput
from .customer import CustomerOutput


class OrderInput(BaseModel):
    customer_id: UUID4
    items: List[OrderItemInput]


class OrderOutput(BaseModel):
    id: UUID4
    customer_id: UUID4
    items: List[OrderItemOutput]
    customer: CustomerOutput

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: UUID
    customer: CustomerOutput
    items: List[OrderItemOutput]
    created_at: datetime

    class Config:
        from_attributes = True

