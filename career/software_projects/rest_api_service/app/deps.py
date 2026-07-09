"""Reusable FastAPI dependencies.

`get_current_user` protects routes: it extracts the bearer token, decodes it,
loads the matching user, and raises 401 on any failure.
"""

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.auth import decode_access_token
from app.database import get_db
from app.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

DbSession = Annotated[Session, Depends(get_db)]


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: DbSession,
) -> User:
    """Resolve the authenticated user from a bearer token or raise 401."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user_id = decode_access_token(token)
    if user_id is None:
        raise credentials_exception

    user = db.get(User, user_id)
    if user is None:
        raise credentials_exception

    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
