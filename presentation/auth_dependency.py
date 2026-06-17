from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from application.auth_service import AuthService

security = HTTPBearer()

auth_service = AuthService()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    return auth_service.get_current_user(token)
