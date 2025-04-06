from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional
from enum import Enum

from app.enums.user_role import UserRole




class UserInput(BaseModel):
    name: str
    email: str
    password: str
    image: Optional[str] = None


class UserOutput(BaseModel):
    id: str
    name: str
    email: str
    image: Optional[str] = None
    role: UserRole

    class Config:
        from_attributes = True


class UserSession(BaseModel):
    id: str
    name: str
    email: str
    image: Optional[str] = None
    role: UserRole
    sub: str
    iat: int
    exp: int
    jti: str

    class Config:
        from_attributes = True
