from app.controllers.sales_person.product import SalesPersonProductController
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from fastapi import Depends
from ...db.db_session_dep import DBSessionDep


def get_sales_person_product_controller(
    db_session: DBSessionDep,
) -> SalesPersonProductController:
    return SalesPersonProductController(db_session)


SalesPersonProductControllerDep = Annotated[
    SalesPersonProductController, Depends(get_sales_person_product_controller)
]
