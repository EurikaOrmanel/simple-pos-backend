from typing import Annotated
from fastapi import Depends

from app.controllers.sales_person.customer import SalesPersonCustomerController
from ...db.db_session_dep import DBSessionDep


def gen_sales_person_customer_controller(db_session: DBSessionDep):
    return SalesPersonCustomerController(db_session)


SalesPersonCustomerControllerDep = Annotated[
    SalesPersonCustomerController,
    Depends(gen_sales_person_customer_controller),
]
