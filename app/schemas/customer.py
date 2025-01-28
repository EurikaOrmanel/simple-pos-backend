from pydantic import BaseModel, Field


class CustomerInput(BaseModel):
    name: str
    phone: str = Field(
        pattern=r"^0(2(0|[3-8])|5(0|[4-7]|9))\d{7}$",
        examples=["0241234567"],
    )
