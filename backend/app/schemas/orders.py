import BaseModel, EmailStr from pydantic

class OrderCreate(BaseModel):
    side : str
    price : int
    quantity : int

class OrderResponse(BaseModel):
    id : int
    side : str
    price : int
    quantity : int
    remaining_quantity : int
    status : str

