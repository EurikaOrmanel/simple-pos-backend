from sqlalchemy import Boolean, Column, String, Enum
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from uuid import uuid4
from ..db.sql_base_class import SqlBase
from ..schemas.user import UserRole


class User(SqlBase):
    __tablename__ = "users"

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

    email = Column(
        String,
        nullable=False,
        unique=True,
    )

    email_verified = Column(
        Boolean,
        default=False,
    )

    password = Column(
        String,
        nullable=False,
    )



    role = Column(
        Enum(UserRole),
        nullable=False,
        default=UserRole.USER,
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        default=datetime.now(timezone.utc),
    )
