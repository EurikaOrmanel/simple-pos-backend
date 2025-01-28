from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, delete
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

class ProductRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, product: ProductCreate) -> Product:
        try:
            db_product = Product(**product.dict())
            self.db_session.add(db_product)
            await self.db_session.commit()
            await self.db_session.refresh(db_product)
            return db_product
        except SQLAlchemyError as e:
            await self.db_session.rollback()
            raise Exception(f"Error creating product: {str(e)}")

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        query = select(Product).where(Product.id == product_id)
        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_all(self) -> List[Product]:
        query = select(Product)
        result = await self.db_session.execute(query)
        return list(result.scalars().all())

    async def update(self, product_id: int, product_update: ProductUpdate) -> Optional[Product]:
        try:
            db_product = await self.get_by_id(product_id)
            if db_product:
                update_data = product_update.dict(exclude_unset=True)
                for field, value in update_data.items():
                    setattr(db_product, field, value)
                await self.db_session.commit()
                await self.db_session.refresh(db_product)
            return db_product
        except SQLAlchemyError as e:
            await self.db_session.rollback()
            raise Exception(f"Error updating product: {str(e)}")

    async def delete(self, product_id: int) -> bool:
        try:
            db_product = await self.get_by_id(product_id)
            if db_product:
                await self.db_session.delete(db_product)
                await self.db_session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            await self.db_session.rollback()
            raise Exception(f"Error deleting product: {str(e)}")
