from ...dependencies.db.db_session_dep import DBSessionDep
from ...repositories.order import OrderRepository


class AdminOrdersController:
    def __init__(self, db_session: DBSessionDep):
        self.db_session = db_session
        self.order_repository = OrderRepository(db_session)

    async def get_orders(
        self,
        page: int,
        limit: int,
    ):
        return await self.order_repository.get_all(page, limit)





