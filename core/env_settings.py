from pydantic_settings import BaseSettings
from functools import lru_cache


class EnvSettings(BaseSettings):

    SQL_DB_USERNAME: str
    SQL_DB_PASSWORD: str
    SQL_DB_HOST: str
    SQL_DB_NAME: str
    SQL_DB_PORT: str
    SQL_TEST_DB_NAME: str
    REFRESH_TOKEN_EXP_MINS: int
    ACCESS_TOKEN_EXP_MIN: int

    class Config:
        env_file = ".env"
        case_sesitive = True
        extra = "ignore"


@lru_cache()
def get_environment_settings() -> EnvSettings:
    return EnvSettings()  # type: ignore


EnvironmentSettings = get_environment_settings()
