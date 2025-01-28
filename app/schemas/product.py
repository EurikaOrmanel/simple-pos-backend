from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class ProductCreateInput(BaseModel):
    name: str
    price: float
    image: str


class ProductUpdateInput(BaseModel):
    name: Optional[str] = Field(default=None)
    price: Optional[float] = Field(default=None)
    image: Optional[str] = Field(default=None)


class ProductOutput(BaseModel):
    id: UUID
    name: str
    price: float
    image: str
    created_at: datetime

    class Config:
        from_attributes = True
