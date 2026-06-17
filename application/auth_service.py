# application/auth_service.py

from datetime import datetime, timedelta

from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException

from infrastructure.user_repository import UserRepositoryImpl


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class AuthService:

    def __init__(self):
        self.user_repository = UserRepositoryImpl()

    def hash_password(
        self,
        password: str
    ):

        return pwd_context.hash(password)

    def verify_password(
        self,
        plain_password: str,
        hashed_password: str
    ):

        return pwd_context.verify(
            plain_password,
            hashed_password
        )

    def create_access_token(
        self,
        user_id: int
    ):

        expire = (
            datetime.utcnow()
            + timedelta(
                minutes=ACCESS_TOKEN_EXPIRE_MINUTES
            )
        )

        payload = {
            "sub": str(user_id),
            "exp": expire
        }

        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm=ALGORITHM
        )

        return token

    def signup(
        self,
        email: str,
        password: str
    ):

        existing_user = (
            self.user_repository
            .get_user_by_email(email)
        )

        if existing_user:
            return None

        hashed_password = self.hash_password(
            password
        )

        user = (
            self.user_repository
            .create_user(
                email=email,
                hashed_password=hashed_password
            )
        )

        return user

    def login(
        self,
        email: str,
        password: str
    ):

        user = (
            self.user_repository
            .get_user_by_email(email)
        )

        if user is None:
            return None

        if not self.verify_password(
            password,
            user.hashed_password
        ):
            return None

        token = self.create_access_token(
            user.id
        )

        return token

    def decode_token(
        self,
        token: str
    ):

        try:

            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=[ALGORITHM]
            )

            user_id = payload.get("sub")

            if user_id is None:
                return None

            return int(user_id)

        except JWTError:
            return None

    def get_current_user(
        self,
        token: str
    ):

        user_id = self.decode_token(token)

        if user_id is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        user = (
            self.user_repository
            .get_user_by_id(user_id)
        )

        if user is None:

            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user
