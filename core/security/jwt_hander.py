from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError, ExpiredSignatureError
from typing import Any
from fastapi import HTTPException
from http import HTTPStatus

from core.customs.simple_exception_type import SimpleExceptionType
from core.customs.simple_exceptions import SimpleException


class JWTHandler:
    def __init__(self, secret: str) -> None:
        self.jwt_secret = secret

    __algorithmn = "HS256"

    def encode(self, payload: dict, exp_min: int) -> str:
        expire = datetime.now(timezone.utc) + timedelta(minutes=exp_min)
        payload.update({"exp": expire})
        return jwt.encode(
            payload,
            self.jwt_secret,
            algorithm=JWTHandler.__algorithmn,
        )

    def decode(self, token: str) -> dict[str, Any]:
        if token:
            try:
                return jwt.decode(
                    token=token,
                    key=self.jwt_secret,
                    algorithms=JWTHandler.__algorithmn,
                    options={"verify_aud": False},
                )
            except ExpiredSignatureError:
                raise SimpleException(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    message="Token has expired",
                    err_type=SimpleExceptionType.TOKEN_EXPIRED,
                )
            except JWTError as e:
                raise SimpleException(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    message="Token error ",
                    err_type=SimpleExceptionType.INVALID_TOKEN_PROVIDED,
                )
        raise SimpleException(
            status_code=HTTPStatus.UNAUTHORIZED,
            message="Invalid token was provided",
            err_type=SimpleExceptionType.INVALID_TOKEN_PROVIDED,
        )
