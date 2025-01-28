from fastapi import APIRouter, Query
from app.dependencies.controllers.sales_person.customer import (
    SalesPersonCustomerControllerDep,
)
from app.models.customer import Customer
from app.schemas.customer import CustomerInput


customer_router = APIRouter(prefix="/customers", tags=["customers"])


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
    customer = Customer(**customer.model_dump())
    return await controller.create_customer(customer)
