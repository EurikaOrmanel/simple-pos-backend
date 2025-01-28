from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ProductInput(BaseModel):
    name: str
    price: float
    image: str


class ProductOutput(BaseModel):
    id: UUID
    name: str
    price: float
    image: str
    created_at: datetime

    class Config:
        from_attributes = True