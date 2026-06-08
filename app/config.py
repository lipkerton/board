from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv()

class Settings(BaseSettings):
    PG_HOST: str
    PG_USER: str
    PG_PASS: str
    PG_PORT: str
    PG_NAME: str

    BASE_DIR: Path = Path('.').absolute()
    TEMPLATES_DIR: Path = Path(BASE_DIR) / "app/templates"
    STATIC_DIR: Path = Path(BASE_DIR) / "app/static"

    @property
    def postgres_url(self):
        return (
            f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASS}"
            f"@{self.PG_HOST}:{self.PG_PORT}/{self.PG_NAME}"
        )   

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8")


settings: Settings = Settings()
    