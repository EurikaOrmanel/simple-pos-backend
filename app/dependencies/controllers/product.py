from typing import Annotated

from fastapi import Depends

from ...controllers.admin.admin_product import AdminProductController



from ..db.db_session_dep import DBSessionDep


def admin_product_controller(db_session: DBSessionDep):
    return AdminProductController(db_session)


AdminProductControllerDep = Annotated[
    AdminProductController, Depends(admin_product_controller)
]
