from fastapi import APIRouter
from .product import product_router
from .auth import admin_auth_router
from .order import order_router

admins_router = APIRouter(prefix="/admins")

admins_router.include_router(admin_auth_router)

admins_router.include_router(product_router)

admins_router.include_router(order_router)