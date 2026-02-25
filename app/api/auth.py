from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import (
    authenticate_user,
    create_token,
    add_token,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
async def login(data: LoginRequest):

    user = authenticate_user(data.username, data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token()
    add_token(token)

    return {
        "access_token": token,
        "token_type": "bearer"
    }