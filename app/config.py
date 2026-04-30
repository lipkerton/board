from dotenv import load_env
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseModel):
    PG_HOST: str
    PG_USER: str
    PG_PASS: str
    PG_PORT: str
    PG_NAME: str

    BASE_DIR: Path = Path('..').absolute()

    @property
    def postgres_url(self):
        return (
            f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASS}"
            f"@{PG_HOST}:{PG_PORT}/{self.PG_NAME}"
        )   

    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", env_file_encoding="utf-8")


settings: Settings = Settings()
    