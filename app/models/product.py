from uuid import UUID, uuid4
from sqlalchemy.orm import relationship
from decimal import Decimal
from sqlalchemy import Column, String, Numeric
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import TIMESTAMP
from app.db.sql_base import SqlBase


class Product(SqlBase):
    __tablename__ = "products"

    id = Column(PostgresUUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    unit_charges = Column(Numeric(10, 2), nullable=False)
    photo_url = Column(String)

    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc),
    )

    order_items = relationship(
        "OrderItem",
        back_populates="product",
        lazy="joined"
    )
