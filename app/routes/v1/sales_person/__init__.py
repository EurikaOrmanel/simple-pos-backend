from fastapi import APIRouter

from .order import order_router
from .customer import customer_router
from .auth import sales_person_auth_router
from .product import product_router


sales_person_router = APIRouter(prefix="/sales_persons")

sales_person_router.include_router(sales_person_auth_router, prefix="/auth")

sales_person_router.include_router(customer_router)

sales_person_router.include_router(order_router)


sales_person_router.include_router(product_router)