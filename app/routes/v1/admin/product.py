from uuid import UUID
from fastapi import APIRouter, Depends, File, Query, UploadFile

from app.controllers.images import ImagesController

from ....dependencies.controllers.product import AdminProductControllerDep
from ....dependencies.user.token_header import handle_user_token
from ....schemas.product import ProductCreateInput, ProductUpdateInput

product_router = APIRouter(
    prefix="/products",
    dependencies=[Depends(handle_user_token)],
)


@product_router.get("/")
async def get_all_products(
    controller: AdminProductControllerDep,
    page: int = Query(1),
    limit: int = Query(10),
):
    return await controller.get_all_products(limit, page)


@product_router.get("/{product_id}")
async def get_product(product_id: UUID,  controller: AdminProductControllerDep):
    return await controller.get_product(product_id)


@product_router.post("/")
async def create_product(
    product: ProductCreateInput, controller: AdminProductControllerDep
):
    return await controller.create_product(product)


@product_router.put("/{product_id}")
async def update_product(
    product_id: UUID, product: ProductUpdateInput, controller: AdminProductControllerDep
):
    return await controller.update_product(product_id, product)


@product_router.delete("/{product_id}")
async def delete_product(product_id: int, controller: AdminProductControllerDep):
    return controller.delete_product(product_id)



@product_router.post("/upload")
async def upload_product_file(
    file: UploadFile = File(...),
):
    return await ImagesController.upload(file)
