from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    username: str
    email: EmailStr
    id: int

class UserLogin(BaseModel):
    email: str
    password: str