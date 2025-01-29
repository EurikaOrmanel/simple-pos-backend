from fastapi import APIRouter, Depends, Query

from app.dependencies.controllers.sales_person.product import (
    SalesPersonProductControllerDep,
)
from app.dependencies.user.token_header import handle_user_token

product_router = APIRouter(
    prefix="/products",
    tags=["products"],
    dependencies=[Depends(handle_user_token)],
)


@product_router.get("/")
async def get_products(
    controller: SalesPersonProductControllerDep,
    page: int = Query(default=1),
    limit: int = Query(default=10),
):
    return await controller.get_all_products(page, limit)
