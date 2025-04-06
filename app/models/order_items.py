from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Float
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from uuid import uuid4
from app.db.sql_base import SqlBase



class OrderItem(SqlBase):
    __tablename__ = "order_items"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        default=uuid4,
    )

    product_id = Column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False
    )

    order_id = Column(
        UUID(as_uuid=True),
        ForeignKey("orders.id"), 
        nullable=False
    )

    quantity = Column(
        Float,
        nullable=False,
        default=1
    )

    order = relationship(
        "Order",
        back_populates="items",
        lazy="selectin"
    )

    product = relationship(
        "Product",
        back_populates="order_items",
        lazy="joined"
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc),
    )
