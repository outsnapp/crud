
# infrastructure/user_repository.py

from domain.user_repository import UserRepository
from domain.user import User

from infrastructure.connection import SessionLocal
from infrastructure.models import User as UserModel


class UserRepositoryImpl(UserRepository):

    def create_user(
        self,
        email: str,
        hashed_password: str
    ):

        session = SessionLocal()

        db_user = UserModel(
            email=email,
            hashed_password=hashed_password
        )

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        session.close()

        return User(
            id=db_user.id,
            email=db_user.email,
            hashed_password=db_user.hashed_password
        )

    def get_user_by_email(
        self,
        email: str
    ):

        session = SessionLocal()

        row = (
            session.query(UserModel)
            .filter(UserModel.email == email)
            .first()
        )

        session.close()

        if row is None:
            return None

        return User(
            id=row.id,
            email=row.email,
            hashed_password=row.hashed_password
        )

    def get_user_by_id(
        self,
        user_id: int
    ):

        session = SessionLocal()

        row = (
            session.query(UserModel)
            .filter(UserModel.id == user_id)
            .first()
        )

        session.close()

        if row is None:
            return None

        return User(
            id=row.id,
            email=row.email,
            hashed_password=row.hashed_password
        )

