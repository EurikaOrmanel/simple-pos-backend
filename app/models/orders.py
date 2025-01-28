from sqlalchemy import Column, ForeignKey, Float, Enum
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from uuid import uuid4
from ..db.sql_base_class import SqlBase
from sqlalchemy.orm import relationship, Mapped
from typing import List


class Order(SqlBase):
    __tablename__ = "orders"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        default=uuid4,
    )

    customer_id = Column(
        UUID(as_uuid=True),
        ForeignKey("customers.id"),
        nullable=False
    )

    total_amount = Column(
        Float,
        nullable=False,
        default=0
    )

    customer = relationship(
        "Customer",
        backref="orders",
        lazy="noload"
    )

    order_items: Mapped[List["OrderItem"]] = relationship(
        "OrderItem",
        backref="order",
        lazy="noload"
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc),
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        nullable=True,
        onupdate=datetime.now(timezone.utc),
    )

    deleted_at = Column(
        TIMESTAMP(timezone=True),
        nullable=True,
    )
