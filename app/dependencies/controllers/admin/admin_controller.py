from typing import Annotated

from fastapi import Depends

from ....controllers.admin.auth import AdminAuthController
from ...db.db_session_dep import DBSessionDep


def admin_controller(db_session: DBSessionDep):
    return AdminAuthController(db_session)


AdminAuthControllerDep = Annotated[
    AdminAuthController,
    Depends(admin_controller),
]
