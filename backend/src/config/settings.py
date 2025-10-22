from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration settings for the codebase QA CLI."""

    alphavantage_api_key: str
    alphavantage_url: str = "https://www.alphavantage.co/query"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = Settings()
