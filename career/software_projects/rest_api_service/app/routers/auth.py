"""Authentication routes: register and login."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth import create_access_token, hash_password, verify_password
from app.deps import DbSession
from app.models import User
from app.schemas import Token, UserCreate, UserRead

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
def register(payload: UserCreate, db: DbSession) -> User:
    """Create a new account. Returns 409 if the email is already taken."""
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    user = User(
        email=payload.email,
        hashed_password=hash_password(payload.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=Token, summary="Obtain an access token")
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: DbSession,
) -> Token:
    """Exchange email + password for a JWT bearer token.

    Uses the OAuth2 password form so the token flow works out-of-the-box in
    the interactive Swagger docs. The `username` field carries the email.
    """
    user = db.query(User).filter(User.email == form_data.username).first()
    if user is None or not verify_password(
        form_data.password, user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(user_id=user.id)
    return Token(access_token=token)
