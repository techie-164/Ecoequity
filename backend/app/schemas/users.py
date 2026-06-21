import BaseModel, EmailStr from pydantic 

class Userregister(BaseModel):
    username : str
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    username : str
    email : EmailStr
    id : int

class Userlogin(BaseModel):
    email : str
    assword : str