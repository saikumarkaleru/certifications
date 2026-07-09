"""User Service — registration and simple token auth.

Passwords are hashed with PBKDF2 (stdlib hashlib) so there are no external
crypto dependencies. Auth issues an opaque, signed token (HMAC) that other
services could verify. Kept deliberately simple but not insecure (no plaintext
passwords, constant-time comparison).
"""
from __future__ import annotations

import hashlib
import hmac
import json
import logging
import os
import secrets
import sqlite3
import sys
import time
from contextlib import contextmanager
from typing import Iterator

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #
SERVICE_NAME = os.getenv("SERVICE_NAME", "user-service")
DB_PATH = os.getenv("DB_PATH", "/tmp/user.db")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
# In real deployments this comes from a k8s Secret, never a default.
SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-change-me")
PBKDF2_ROUNDS = int(os.getenv("PBKDF2_ROUNDS", "100000"))


# --------------------------------------------------------------------------- #
# Structured JSON logging
# --------------------------------------------------------------------------- #
class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(record.created)),
            "level": record.levelname,
            "service": SERVICE_NAME,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload)


def _build_logger() -> logging.Logger:
    logger = logging.getLogger(SERVICE_NAME)
    logger.setLevel(LOG_LEVEL)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    logger.handlers = [handler]
    logger.propagate = False
    return logger


log = _build_logger()


# --------------------------------------------------------------------------- #
# Password + token helpers (stdlib only)
# --------------------------------------------------------------------------- #
def hash_password(password: str, salt: str | None = None) -> str:
    salt = salt or secrets.token_hex(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), PBKDF2_ROUNDS)
    return f"{salt}${dk.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        salt, _ = stored.split("$", 1)
    except ValueError:
        return False
    return hmac.compare_digest(hash_password(password, salt), stored)


def issue_token(username: str) -> str:
    body = f"{username}:{int(time.time())}"
    sig = hmac.new(SECRET_KEY.encode(), body.encode(), hashlib.sha256).hexdigest()
    return f"{body}:{sig}"


def verify_token(token: str) -> str:
    try:
        username, ts, sig = token.rsplit(":", 2)
        body = f"{username}:{ts}"
    except ValueError:
        raise HTTPException(status_code=401, detail="malformed token")
    expected = hmac.new(SECRET_KEY.encode(), body.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(sig, expected):
        raise HTTPException(status_code=401, detail="invalid token")
    return username


# --------------------------------------------------------------------------- #
# Database
# --------------------------------------------------------------------------- #
@contextmanager
def get_db() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db() -> None:
    with get_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                username      TEXT    NOT NULL UNIQUE,
                password_hash TEXT    NOT NULL
            )
            """
        )
    log.info("database initialised at %s", DB_PATH)


# --------------------------------------------------------------------------- #
# Schemas
# --------------------------------------------------------------------------- #
class Credentials(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6, max_length=128)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserPublic(BaseModel):
    id: int
    username: str


# --------------------------------------------------------------------------- #
# App
# --------------------------------------------------------------------------- #
app = FastAPI(title="User Service", version="1.0.0")


@app.on_event("startup")
def _startup() -> None:
    init_db()
    if SECRET_KEY == "dev-only-change-me":
        log.warning("SECRET_KEY is the insecure default — set it via a Secret in prod")
    log.info("%s started", SERVICE_NAME)


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok", "service": SERVICE_NAME}


@app.get("/readyz")
def readyz() -> dict:
    try:
        with get_db() as conn:
            conn.execute("SELECT 1")
        return {"status": "ready", "service": SERVICE_NAME}
    except Exception as exc:  # pragma: no cover - defensive
        raise HTTPException(status_code=503, detail=f"not ready: {exc}")


@app.post("/register", response_model=UserPublic, status_code=201)
def register(creds: Credentials) -> UserPublic:
    try:
        with get_db() as conn:
            cur = conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?,?)",
                (creds.username, hash_password(creds.password)),
            )
            uid = cur.lastrowid
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="username already exists")
    log.info("registered user id=%s username=%s", uid, creds.username)
    return UserPublic(id=uid, username=creds.username)


@app.post("/login", response_model=TokenResponse)
def login(creds: Credentials) -> TokenResponse:
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE username = ?", (creds.username,)
        ).fetchone()
    if row is None or not verify_password(creds.password, row["password_hash"]):
        log.warning("failed login for username=%s", creds.username)
        raise HTTPException(status_code=401, detail="invalid credentials")
    log.info("successful login username=%s", creds.username)
    return TokenResponse(access_token=issue_token(creds.username))


@app.get("/me", response_model=UserPublic)
def me(authorization: str = Header(default="")) -> UserPublic:
    if not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=401, detail="missing bearer token")
    token = authorization.split(" ", 1)[1]
    username = verify_token(token)
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
    if row is None:
        raise HTTPException(status_code=401, detail="unknown user")
    return UserPublic(id=row["id"], username=row["username"])
