from fastapi import APIRouter, Depends, Query
from app.dependencies.controllers.sales_person.customer import (
    SalesPersonCustomerControllerDep,
)
from app.dependencies.user.token_header import handle_user_token
from app.models.customer import Customer
from app.schemas.customer import CustomerInput


customer_router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    dependencies=[Depends(handle_user_token)],
)


@customer_router.get("/suggest")
async def suggest_customers(
    controller: SalesPersonCustomerControllerDep,
    q: str = Query(default=""),
):
    return await controller.suggest_customers(q)


@customer_router.post("/")
async def create_customer(
    controller: SalesPersonCustomerControllerDep,
    customer: CustomerInput,
):
    return await controller.create_customer(customer)
