from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.models.order import Order
from app.models.order_items import OrderItem


class OrderRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_order(self, order: Order) -> Order:
        try:
            self.db.add(order)
            await self.db.commit()
            await self.db.refresh(order)
            return order
        except SQLAlchemyError as e:
            await self.db.rollback()
            raise Exception(f"Failed to create order: {str(e)}")

    async def get_order_by_id(self, order_id: UUID) -> Order:
        try:
            stmt = (
                select(Order)
                .options(
                    selectinload(Order.customer),
                    selectinload(Order.items).selectinload(OrderItem.product)
                )
                .where(Order.id == order_id)
            )
            result = await self.db.execute(stmt)
            return result.unique().scalar_one_or_none()
        except SQLAlchemyError as e:
            raise Exception(f"Failed to get order: {str(e)}")
