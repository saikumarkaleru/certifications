"""Application configuration loaded from environment variables.

Uses pydantic-settings so every setting can be overridden via env vars or a
`.env` file. This keeps secrets (JWT key) and environment-specific values
(database URL) out of the source code.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Strongly-typed application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # General
    app_name: str = "Task Manager API"
    environment: str = "development"
    debug: bool = True

    # Database
    database_url: str = "sqlite:///./tasks.db"

    # Auth / JWT
    secret_key: str = "CHANGE_ME_IN_PRODUCTION_use_a_long_random_string"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance (loaded once per process)."""
    return Settings()


settings = get_settings()
