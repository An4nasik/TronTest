from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict
class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()
