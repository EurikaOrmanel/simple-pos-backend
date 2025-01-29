from app.repositories.product import ProductRepository
from sqlalchemy.ext.asyncio import AsyncSession


class SalesPersonProductController:
    def __init__(self, db_session: AsyncSession):
        self.product_repo = ProductRepository(db_session)

    async def get_all_products(self, page: int, limit: int):
        return await self.product_repo.get_all(limit, page)
