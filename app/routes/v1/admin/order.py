from fastapi import APIRouter, Depends, File, Query, UploadFile
from app.controllers.images import ImagesController
from app.dependencies.controllers.admin.order import AdminOrdersControllerDep
from app.dependencies.user.token_header import handle_user_token


order_router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    dependencies=[
        Depends(handle_user_token),
    ],
)


@order_router.get("/")
async def get_orders(
    controller: AdminOrdersControllerDep,
    page: int = Query(1),
    limit: int = Query(10),
):
    return await controller.get_orders(page, limit)

