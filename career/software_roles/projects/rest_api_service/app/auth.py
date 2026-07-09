"""Authentication helpers: password hashing and JWT creation/decoding.

Passwords are hashed with bcrypt (via passlib). Tokens are signed JWTs
containing the user id (`sub`) and an expiry (`exp`).
"""

from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext

from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    """Return a bcrypt hash for a plaintext password."""
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a plaintext password against a stored bcrypt hash."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    user_id: int, expires_delta: timedelta | None = None
) -> str:
    """Create a signed JWT access token for the given user id."""
    expire = datetime.now(timezone.utc) + (
        expires_delta
        or timedelta(minutes=settings.access_token_expire_minutes)
    )
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def decode_access_token(token: str) -> int | None:
    """Return the user id encoded in a valid token, or None if invalid."""
    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        subject = payload.get("sub")
        if subject is None:
            return None
        return int(subject)
    except (jwt.PyJWTError, ValueError):
        return None
