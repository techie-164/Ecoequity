from sqlalchemy.orm import Session
from backend.app.models.users import User
from backend.app.utils.jwt import verify_access_token

def get_current_user(db: Session, token: str):
    username = verify_access_token(token)
    if username is None:
        return None
    user = db.query(User).filter(User.username == username).first()
    return user

