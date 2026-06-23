from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from backend.app.utils.hashing import hash_password
from backend.app.schemas.users import UserRegister
from backend.app.models.users import User
from backend.app.db import get_db
from backend.app.schemas.users import UserLogin
from backend.app.models.users import User
from backend.app.utils.hashing import verify_password
from backend.app.utils.jwt import create_access_token


router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"]
)

@router.post("/register")
def register(user : UserRegister, db : Session = Depends(get_db)):  
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password), 
        role="User"
    )

    db.add(new_user)
    db.commit()

    return{
        "message" : "User created successfully"
    }

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        return {
            "message": "User not found"
        }

    if not verify_password(
        user.password,
        db_user.password_hash
    ):
        return {
            "message": "Invalid Password"
        }

    token = create_access_token(
        {
        "sub" : db_user.username
        }
    )
    return {
        "access_token": token,
        "token_type": "bearer"
    }