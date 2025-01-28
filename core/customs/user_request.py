from starlette.requests import empty_receive, empty_send
from app.models.user import User
from starlette.types import Receive, Scope, Send
from typing import Union
from fastapi import Request


class UserRequest(Request):
    def __init__(
        self,
        user: User,
        user_id: str | None,
        scope: Scope,
        receive: Receive = ...,
        send: Send = ...,
    ):
        super().__init__(scope, receive, send)
        self.current_user = user
        self.user_id: str | None = user_id
