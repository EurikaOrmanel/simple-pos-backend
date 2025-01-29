from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.customer import CustomerRepository
from app.schemas.customer import CustomerInput


class SalesPersonCustomerController:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.customer_repository = CustomerRepository(db_session)

    async def suggest_customers(self, keyword: str):
        return await self.customer_repository.search_customers(keyword)

    async def create_customer(self, customer: CustomerInput):
        customer = await self.customer_repository.find_by_phone(customer.phone)
        if customer:
            return customer
        return await self.customer_repository.create_customer(customer)
    