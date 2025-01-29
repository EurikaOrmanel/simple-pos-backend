from http import HTTPStatus
from typing import Annotated
from fastapi import Header

from app.dependencies.db.db_session_dep import DBSessionDep
from app.enums.user_role import UserRole
from ...repositories.user import UserRepository
from core.customs.simple_exception_type import SimpleExceptionType
from core.customs.simple_exceptions import SimpleException
from core.customs.user_request import UserRequest
from core.env_settings import EnvironmentSettings
from core.security.jwt_hander import JWTHandler


jwt_handler = JWTHandler(EnvironmentSettings.USER_TOKEN_SECRET)


async def handle_user_token(
    request: UserRequest,
    authorization: Annotated[str, Header()],
    db_session: DBSessionDep,
):
    decoded_token = jwt_handler.decode(authorization)

    if "id" in decoded_token:
        request.user_id = decoded_token["id"]

        request.current_user = await UserRepository(db_session).find_by_id(
            decoded_token["id"]
        )
        if "/admin" in request.url.path and request.current_user.role != UserRole.ADMIN:
            raise SimpleException(
                status_code=HTTPStatus.FORBIDDEN,
                message="You are not authorized to access this resource",
            )
    else:
        raise SimpleException(
            status_code=HTTPStatus.UNAUTHORIZED,
            message="Invalid token provided",
            err_type=SimpleExceptionType.INVALID_TOKEN_PROVIDED,
        )
