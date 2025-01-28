from sqlalchemy import Column, String, Float
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from uuid import uuid4
from app.db.sql_base import SqlBase


class Product(SqlBase):
    __tablename__ = "products"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        default=uuid4,
    )

    name = Column(
        String(100),
        nullable=False,
    )

    price = Column(
        Float,
        nullable=False,
    )

    image = Column(
        String,
        nullable=True,
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc),
    )
