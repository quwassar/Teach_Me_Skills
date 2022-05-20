from pydantic import BaseSettings


class Config(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWD: str
    SECRET_KEY: str

    class Config:
        env_file = '.env'


config = Config()
