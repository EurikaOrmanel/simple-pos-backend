from fastapi import APIRouter
from .product import product_router

admins_router = APIRouter(prefix="/admins")

admins_router.include_router(product_router)
