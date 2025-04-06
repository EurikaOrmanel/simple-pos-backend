from http import HTTPStatus
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.customer import Customer
from app.repositories.customer import CustomerRepository
from app.schemas.customer import CustomerInput
from core.customs.simple_exception_type import SimpleExceptionType
from core.customs.simple_exceptions import SimpleException


class SalesPersonCustomerController:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.customer_repository = CustomerRepository(db_session)

    async def suggest_customers(self, keyword: str):
        return await self.customer_repository.search_customers(keyword)

    async def create_customer(self, body: CustomerInput):
        customer = await self.customer_repository.find_by_phone(body.phone)
        if customer:
            raise SimpleException(
                status_code=HTTPStatus.BAD_REQUEST,
                message="Customer with this phone number already exists",
                err_type=SimpleExceptionType.ALREADY_EXISTS,
            )
        return await self.customer_repository.create_customer(Customer(**body.model_dump()))
