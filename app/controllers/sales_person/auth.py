from http import HTTPStatus
from uuid import UUID
from app.controllers.admin.auth import AdminAuthController
from app.dependencies.db.db_session_dep import DBSessionDep
from app.repositories.user import UserRepository
from app.schemas.sales_person import (
    SalesPersonLoginInput,
    SalesPersonLoginOutput,
    SalesPersonRegisterInput,
)
from core.customs.simple_exceptions import SimpleException
from core.env_settings import EnvironmentSettings
from core.security.jwt_hander import JWTHandler
from core.security.password_handler import PasswordHandler
from sqlalchemy.ext.asyncio import AsyncSession


class SalesPersonAuthController:
    __jwt_handler = JWTHandler(EnvironmentSettings.USER_TOKEN_SECRET)

    def __init__(
        self,
        db_session: AsyncSession,
    ):
        self.db_session = db_session
        self.user_repository = UserRepository(db_session)

    async def login(self, body: SalesPersonLoginInput):
        user = await self.user_repository.find_by_email(body.email)
        if not user:
            raise SimpleException(HTTPStatus.NOT_FOUND, "User not found")
        if not PasswordHandler.verify(body.password, user.password):
            raise SimpleException(
                HTTPStatus.UNAUTHORIZED,
                "Wrong password",
            )

        return SalesPersonAuthController.__generate_response(str(user.id))

    async def register(self, body: SalesPersonRegisterInput):
        user = await self.user_repository.find_by_email(body.email)
        if user:
            raise SimpleException(HTTPStatus.CONFLICT, "User already exists")

        body.password = PasswordHandler.hash(body.password)
        user = await self.user_repository.create(body)
        return AdminAuthController.__generate_response(str(user.id))

    @staticmethod
    def __generate_response(user_id: UUID) -> SalesPersonLoginOutput:
        access_token = SalesPersonAuthController.__jwt_handler.encode(
            {"id": str(user_id)},
            EnvironmentSettings.ACCESS_TOKEN_EXP_MIN,
        )

        return SalesPersonLoginOutput(
            access_token=access_token,
        )
