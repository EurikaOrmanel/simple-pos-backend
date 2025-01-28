from pydantic import BaseModel


class AdminLoginInput(BaseModel):
    email: str
    password: str


class AdminLoginOutput(BaseModel):
    access_token: str



class AdminRegisterInput(BaseModel):
    email: str
    password: str
    name: str
