from http import HTTPStatus
from uuid import UUID

from app.models.product import Product
from core.customs.simple_exception_type import SimpleExceptionType
from ...dependencies.db.db_session_dep import DBSessionDep
from ...repositories.product import ProductRepository
from ...schemas.product import ProductCreateInput, ProductUpdateInput
from core.customs.simple_exceptions import SimpleException


class AdminProductController:
    def __init__(self, db_session: DBSessionDep):
        self.product_repo = ProductRepository(db_session)
        self.db_session = db_session

    async def create_product(self, product: ProductCreateInput):
        # Check if product already exists (assuming name is unique)
        existing_product = await self.product_repo.get_by_name(product.name)
        if existing_product:
            raise SimpleException(
                status_code=HTTPStatus.BAD_REQUEST,
                message="Product with this name already exists",
                err_type=SimpleExceptionType.ALREADY_EXISTS,
            )
        return await self.product_repo.create(Product(**product.model_dump()))

    async def get_product(
        self,
        product_id: UUID,
    ):
        product = await self.product_repo.get_by_id(product_id)
        if not product:
            raise SimpleException(
                HTTPStatus.NOT_FOUND, "Product not found", SimpleExceptionType.NOT_FOUND
            )
        return product

    async def get_all_products(self, limit: int = 10, page: int = 1):
        products = await self.product_repo.get_all(limit, page)
        if not products:
            return []  # Return empty list instead of error for get_all
        return products

    async def update_product(
        self,
        product_id: UUID,
        product: ProductUpdateInput,
    ):
        existing_product = await self.product_repo.get_by_id(product_id)
        if not existing_product:
            raise SimpleException("Product not found")
        return await self.product_repo.update(product_id, product.model_dump())

    async def delete_product(self, product_id: UUID):
        existing_product = await self.product_repo.get_by_id(product_id)
        if not existing_product:
            raise SimpleException("Product not found")
        return await self.product_repo.delete(product_id)
