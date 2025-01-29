from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order_items import OrderItem
from app.repositories.order_item import OrderItemRepository

from ...models.order import Order
from ...schemas.order import OrderInput

from ...repositories.order import OrderRepository


class SalesPersonOrderController:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.order_repository = OrderRepository(db_session)
        self.order_item_repository = OrderItemRepository(db_session)

    async def create_order(self, order: OrderInput):
        order_items = [OrderItem(**item.model_dump()) for item in order.items]
        order = Order(
            items=order_items,
            customer_id=order.customer_id,
        )
        order=await self.order_repository.create_order(order)
        await self.order_item_repository.create_order_items(order_items)
        return await self.order_repository.get_order_by_id(order.id)

    async def get_order(self, order_id: UUID):
        return await self.order_repository.get_order_by_id(order_id)
