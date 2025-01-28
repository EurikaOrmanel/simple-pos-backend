from fastapi import APIRouter
from .admin import admins_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(admins_router)
