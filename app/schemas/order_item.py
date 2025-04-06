from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from .product import ProductResponse

class OrderItemOutput(BaseModel):
    id: UUID
    product: ProductResponse
    quantity: float
    created_at: datetime

    class Config:
        from_attributes = True

class OrderItemInput(BaseModel):
    product_id: UUID
    quantity: float
