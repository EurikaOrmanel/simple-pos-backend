from sqlalchemy import Column, ForeignKey, Float, Enum
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from uuid import uuid4
from app.db.sql_base import SqlBase
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

    customer = relationship(
        "Customer",
        backref="orders",
        lazy="selectin"
    )

    items = relationship(
        "OrderItem",
        back_populates="order",
        lazy="selectin",
        join_depth=2  # This ensures nested relationships are loaded
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
