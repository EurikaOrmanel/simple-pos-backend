from fastapi import APIRouter, Depends

from ....dependencies.controllers.product import AdminProductControllerDep
from ....dependencies.user.token_header import handle_user_token
from ....schemas.product import ProductCreateInput, ProductUpdateInput

product_router = APIRouter(
    prefix="/products",
    dependencies=[Depends(handle_user_token)],
)


@product_router.get("/")
async def get_all_products(controller: AdminProductControllerDep):
    return controller.get_all_products()


@product_router.get("/{product_id}")
async def get_product(product_id: int, controller: AdminProductControllerDep):
    return controller.get_product(product_id)


@product_router.post("/")
async def create_product(
    product: ProductCreateInput, controller: AdminProductControllerDep
):
    return controller.create_product(product)


@product_router.put("/{product_id}")
async def update_product(
    product_id: int, product: ProductUpdateInput, controller: AdminProductControllerDep
):
    return controller.update_product(product_id, product)


@product_router.delete("/{product_id}")
async def delete_product(product_id: int, controller: AdminProductControllerDep):
    return controller.delete_product(product_id)
