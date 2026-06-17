# domain/user.py

class User:

    def __init__(
        self,
        id: int,
        email: str,
        hashed_password: str
    ):
        self.id = id
        self.email = email
        self.hashed_password = hashed_password

    def to_dict(self):

        return {
            "id": self.id,
            "email": self.email
        }
