from fastapi import APIRouter, Query
from app.dependencies.controllers.admin.order import AdminOrdersControllerDep


order_router = APIRouter(prefix="/orders", tags=["orders"])


@order_router.get("/")
async def get_orders(
    controller: AdminOrdersControllerDep,
    page: int = Query(1),
    limit: int = Query(10),
):
    return await controller.get_orders(page, limit)
