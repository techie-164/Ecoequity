import BaseModel, EmailStr from pydantic 

class UserregisterSchema(BaseModel):
    username : str
    email : EmailStr
    password : str

class UserResponseSchema(BaseModel):
    username : str
    email : EmailStr
    id : int
