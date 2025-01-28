from fastapi import APIRouter
from .auth import sales_person_auth_router


sales_person_router = APIRouter(prefix="/sales_persons")

sales_person_router.include_router(sales_person_auth_router, prefix="/auth")
