from fastapi import FastAPI
import uvicorn 
from backend.app.models.users import User
from backend.app.db import Base, engine
from backend.app.routes.auth import router as auth_router 

# Create Table 
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="EcoEquity API",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to EcoEquity"
    }