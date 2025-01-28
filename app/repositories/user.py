from sqlalchemy.future import select
from uuid import UUID
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

async def get_user_by_id(self, user_id: UUID):
    stmt = select(User).where(User.id == user_id)
    result = await self.session.execute(stmt)
    return result.scalar_one_or_none()


