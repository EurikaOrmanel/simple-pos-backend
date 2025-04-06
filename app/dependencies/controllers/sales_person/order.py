from typing import Annotated
from fastapi import Depends

from ....controllers.sales_person.order import SalesPersonOrderController
from ....dependencies.db.db_session_dep import DBSessionDep



def get_order_controller(db_session: DBSessionDep):
    return SalesPersonOrderController(db_session)


SalesPersonOrderControllerDep = Annotated[
    SalesPersonOrderController, Depends(get_order_controller)
]
