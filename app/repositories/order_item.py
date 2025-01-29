from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.order_items import OrderItem


class OrderItemRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session


    async def create_order_item(self, order_item: OrderItem):
        try:
            self.db_session.add(order_item)
            await self.db_session.commit()
            await self.db_session.refresh(order_item)
            return order_item
        except SQLAlchemyError as e:
            await self.db_session.rollback()
            raise Exception(f"Error creating order item: {str(e)}")
    async def create_order_items(self, order_items: List[OrderItem]):
        try:
            self.db_session.add_all(order_items)
            await self.db_session.commit()
        except SQLAlchemyError as e:
            await self.db_session.rollback()
            raise Exception(f"Error creating order items: {str(e)}")
