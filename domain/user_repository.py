
# domain/user_repository.py

from abc import ABC, abstractmethod

from domain.user import User


class UserRepository(ABC):

    @abstractmethod
    def create_user(
        self,
        email: str,
        hashed_password: str
    ) -> User:
        pass

    @abstractmethod
    def get_user_by_email(
        self,
        email: str
    ) -> User | None:
        pass

    @abstractmethod
    def get_user_by_id(
        self,
        user_id: int
    ) -> User | None:
        pass

