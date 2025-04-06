from fastapi import APIRouter

from app.dependencies.controllers.sales_person.auth import SalesPersonAuthControllerDep
from app.schemas.sales_person import SalesPersonLoginInput, SalesPersonRegisterInput


sales_person_auth_router = APIRouter()


@sales_person_auth_router.post("/login", tags=["Sales Person Auth"])
async def login(
    body: SalesPersonLoginInput,
    controller: SalesPersonAuthControllerDep,
):
    return await controller.login(body)


@sales_person_auth_router.post("/register", tags=["Sales Person Auth"])
async def register(
    body: SalesPersonRegisterInput,
    controller: SalesPersonAuthControllerDep,
):
    return await controller.register(body)
