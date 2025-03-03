"""
Authentication config module
"""

from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend
from fastapi_users import FastAPIUsers
from src.users.models import User

from src.users.manager import get_user_manager

from src.environs import JWT_SECRET


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=JWT_SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])
current_user = fastapi_users.current_user(active=True)

