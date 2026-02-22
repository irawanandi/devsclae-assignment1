from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Assignment 1"
    VERSION: str = "0.0.1"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
