from fastapi import APIRouter

router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"]
)

@router.post("/register")
def register():
    return{
        "Message" : "Auth router working"
    }

@router.post("/login")
def login():
    return {
        "Message" : "Login router working"
    }