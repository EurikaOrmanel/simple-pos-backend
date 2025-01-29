from typing import Annotated

from fastapi import Depends
from app.controllers.admin.admin_orders import AdminOrdersController
from app.dependencies.db.db_session_dep import DBSessionDep


def get_admin_order_controller(db_session: DBSessionDep):
    return AdminOrdersController(db_session)


AdminOrdersControllerDep = Annotated[
    AdminOrdersController,
    Depends(get_admin_order_controller),
]
