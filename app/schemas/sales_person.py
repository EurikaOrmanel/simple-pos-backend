from uuid import UUID
from pydantic import BaseModel


class SalesPersonLoginInput(BaseModel):
    email: str
    password: str


class SalesPersonRegisterInput(BaseModel):
    email: str
    password: str
    name: str


class SalesPersonLoginOutput(BaseModel):
    access_token: str
