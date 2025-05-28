from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    stripe_secret_key: str
    stripe_publishable_key: str

    class Config:
        env_file = '.env'

settings = Settings()