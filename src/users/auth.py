"""
<<<<<<< HEAD
Authentication
"""

from fastapi_users.authentication import (
    BearerTransport,
    JWTStrategy,
    AuthenticationBackend
)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

SECRET = "SECRET"

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)
=======
Authentication config module
"""

from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend

from src.environs import JWT_SECRET

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=JWT_SECRET, lifetime_seconds=3600)
>>>>>>> 2cb9f00 (Authorization and registration for users)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
<<<<<<< HEAD
)
=======
)
>>>>>>> 2cb9f00 (Authorization and registration for users)
