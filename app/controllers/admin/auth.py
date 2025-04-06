from datetime import datetime, timedelta, timezone

from http import HTTPStatus
from uuid import UUID
from app.dependencies.db.db_session_dep import DBSessionDep
from app.repositories.user import UserRepository
from app.schemas.admin_auth import AdminLoginInput, AdminLoginOutput, AdminRegisterInput
from app.schemas.user import UserRole
from core.customs.simple_exceptions import SimpleException
from core.env_settings import EnvironmentSettings
from core.security.jwt_hander import JWTHandler
from core.security.password_handler import PasswordHandler


class AdminAuthController:
    __jwt_handler = JWTHandler(EnvironmentSettings.USER_TOKEN_SECRET)

    def __init__(self, db_session: DBSessionDep):
        self.db_session = db_session
        self.user_repository = UserRepository(db_session)

    async def login(self, body: AdminLoginInput):
        user = await self.user_repository.find_by_email(body.email)
        if not user:
            raise SimpleException(401, "Invalid credentials")
        if user.role != UserRole.ADMIN:
            raise SimpleException(
                HTTPStatus.UNAUTHORIZED,
                "User is not an admin",
            )
        if not PasswordHandler.verify(body.password, user.password):
            raise SimpleException(
                HTTPStatus.UNAUTHORIZED,
                "Wrong password",
            )
        return AdminAuthController.__generate_response(str(user.id))

    async def register(self, body: AdminRegisterInput):
        user = await self.user_repository.find_by_email(body.email)
        if user:
            raise SimpleException(401, "User already exists")

        body.password = PasswordHandler.hash(body.password)
        user = await self.user_repository.create(body)
        return AdminAuthController.__generate_response(str(user.id))

    @staticmethod
    def __generate_response(user_id: UUID) -> AdminLoginOutput:
        access_token = AdminAuthController.__jwt_handler.encode(
            {"id": str(user_id)},
            EnvironmentSettings.ACCESS_TOKEN_EXP_MIN,
        )

        return AdminLoginOutput(
            access_token=access_token,
        )
