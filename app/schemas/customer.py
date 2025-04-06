from pydantic import UUID4, BaseModel, Field


class CustomerInput(BaseModel):
    name: str
    phone: str = Field(
        pattern=r"^0(2(0|[3-8])|5(0|[4-7]|9))\d{7}$",
        examples=["0241234567"],
    )



class CustomerOutput(BaseModel):
    id: UUID4
    name: str
    phone: str

    class Config:
        from_attributes = True