from typing import Optional
from sqlalchemy.future import select
from uuid import UUID
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from app.enums.user_role import UserRole
from app.models.user import User
from app.schemas.admin_auth import AdminRegisterInput
from app.schemas.sales_person import SalesPersonRegisterInput


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, user_id: UUID):
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, user_input: SalesPersonRegisterInput | AdminRegisterInput):
        user = User(**user_input.model_dump())
        if isinstance(user_input, AdminRegisterInput):
            user.role = UserRole.ADMIN
        elif isinstance(user, SalesPersonRegisterInput):
            user.role = UserRole.USER
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def find_by_id(self, user_id: UUID):
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def find_by_email(self, email: str) -> Optional[User]:
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()
