from sqlalchemy import select, delete
from typing import List, Optional, Union
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from app.models.customer import Customer


class CustomerRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def search_customers(self, keyword: str) -> List[Customer]:
        query = select(Customer).where(Customer.name.ilike(f"%{keyword}%"))
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def create_customer(self, customer: Customer) -> Customer:
        try:
            self.db_session.add(customer)
            await self.db_session.commit()
            await self.db_session.refresh(customer)
            return customer
        except SQLAlchemyError as e:
            await self.db_session.rollback()
            raise Exception(f"Error creating customer: {str(e)}")

    async def find_by_phone(self, phone: str) -> Optional[Customer]:
        query = select(Customer).where(Customer.phone == phone)
        result = await self.db_session.execute(query)
        return result.scalars().first()
