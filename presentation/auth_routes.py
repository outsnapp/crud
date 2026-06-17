# presentation/auth_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from application.auth_service import AuthService
from fastapi import Depends

from presentation.auth_dependency import get_current_user
from domain.user import User


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

auth_service = AuthService()


class SignupRequest(BaseModel):
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/signup")
def signup(request: SignupRequest):

    user = auth_service.signup(
        email=request.email,
        password=request.password
    )

    if user is None:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    return {
        "message": "User created successfully",
        "user": user.to_dict()
    }


@router.post("/login")
def login(request: LoginRequest):

    token = auth_service.login(
        email=request.email,
        password=request.password
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):

    return current_user.to_dict()
