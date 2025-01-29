from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ....controllers.sales_person.order import SalesPersonOrderController
from ....dependencies.db.db_session_dep import DBSessionDep

from ....repositories.order import OrderRepository


def get_order_repository(db_session: DBSessionDep):
    return SalesPersonOrderController(db_session)


SalesPersonOrderControllerDep = Annotated[
    OrderRepository, Depends(get_order_repository)
]
