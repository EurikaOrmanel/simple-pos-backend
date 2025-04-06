from fastapi import APIRouter, Request

from ....schemas.admin_auth import AdminLoginInput, AdminLoginOutput, AdminRegisterInput

from ....dependencies.controllers.admin.admin_controller import AdminAuthControllerDep


admin_auth_router = APIRouter(prefix="/auth")


@admin_auth_router.post(
    "/login",
    response_model=AdminLoginOutput,
)
async def login(
    request: AdminLoginInput,
    controller: AdminAuthControllerDep,
):
    return await controller.login(request)


@admin_auth_router.post(
    "/register",
    response_model=AdminLoginOutput,
)
async def register(
    request: AdminRegisterInput,
    controller: AdminAuthControllerDep,
):
    return await controller.register(request)
