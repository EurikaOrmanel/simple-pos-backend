from typing import Annotated
from fastapi import Depends

from app.controllers.sales_person.auth import SalesPersonAuthController
from app.dependencies.db.db_session_dep import DBSessionDep


def gen_sales_person_auth_controller(db_session: DBSessionDep):
    return SalesPersonAuthController(db_session)


SalesPersonAuthControllerDep = Annotated[
    SalesPersonAuthController,
    Depends(gen_sales_person_auth_controller),
]
