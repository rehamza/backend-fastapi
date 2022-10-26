from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Short Url App"
    HOST: str
    PORT: int
    ORIGIN_URL1: str
    ENV: str



    class Config:
        env_file = ".env"