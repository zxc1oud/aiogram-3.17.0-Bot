from pydantic import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    USER: str
    PASSWORD: str
    NAME: str
    HOST: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()