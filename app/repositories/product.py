from typing import List, Optional, Union, Dict, Any
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, delete, update
from app.models.product import Product
from app.schemas.product import ProductCreateInput, ProductUpdateInput


class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, product: Product) -> Product:
        try:
            self.db.add(product)
            await self.db.commit()
            await self.db.refresh(product)
            return product
        except SQLAlchemyError as e:
            await self.db.rollback()
            raise Exception(f"Failed to create product: {str(e)}")

    async def get_by_id(self, product_id: UUID) -> Optional[Product]:
        stmt = select(Product).filter(Product.id == product_id)
        result = await self.db.execute(stmt)
        return result.unique().scalar_one_or_none()

    async def get_all(self, limit: int = 10, page: int = 1) -> List[Product]:
        offset = (page - 1) * limit
        query = select(Product).limit(limit).offset(offset)
        result = await self.db.execute(query)
        return result.scalars().unique().all()

    async def update(self, product_id: UUID, data: Dict[str, Any]) -> Optional[Product]:
        try:
            stmt = (
                update(Product)
                .where(Product.id == product_id)
                .values(**data)
                .returning(Product)
            )
            result = await self.db.execute(stmt)
            await self.db.commit()
            return result.scalar_one()
        except SQLAlchemyError as e:
            await self.db.rollback()
            raise Exception(f"Failed to update product: {str(e)}")

    async def delete(self, product_id: UUID) -> bool:
        try:
            db_product = await self.get_by_id(product_id)
            if db_product:
                await self.db.delete(db_product)
                await self.db.commit()
                return True
            return False
        except SQLAlchemyError as e:
            await self.db.rollback()
            raise Exception(f"Error deleting product: {str(e)}")

    async def get_by_name(self, name: str) -> Union[Product, None]:
        query = select(Product).where(Product.name == name)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()
