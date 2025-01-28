from sqlalchemy import Column, String
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from uuid import uuid4
from ..db.sql_base_class import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        default=uuid4,
    )

    full_name = Column(
        String(200),
        nullable=False,
    )

    phone_number = Column(
        String,
        nullable=False,
        unique=True,
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

