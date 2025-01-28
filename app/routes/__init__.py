from .v1 import v1_router
from fastapi import APIRouter

api_routers = APIRouter(prefix="")

api_routers.include_router(v1_router)
