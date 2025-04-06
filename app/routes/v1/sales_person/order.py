from uuid import UUID
from fastapi import APIRouter, Depends

from app.dependencies.controllers.sales_person.order import (
    SalesPersonOrderControllerDep,
)
from app.dependencies.user.token_header import handle_user_token
from app.schemas.order import OrderInput, OrderOutput, OrderResponse


order_router = APIRouter(
    prefix="/orders",
    tags=["order"],
    dependencies=[Depends(handle_user_token)],
)


@order_router.post(
    "/create",
    response_model=OrderOutput,
)
async def create_order(
    order: OrderInput,
    order_controller: SalesPersonOrderControllerDep,
):
    return await order_controller.create_order(order)


@order_router.get(
    "/{order_id}",
    response_model=OrderOutput,
)
async def get_order(
    order_id: UUID,
    controller: SalesPersonOrderControllerDep,
):
    return await controller.get_order(order_id)
