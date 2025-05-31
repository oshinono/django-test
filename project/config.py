from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    stripe_usd_secret_key: str
    stripe_usd_publishable_key: str
    stripe_rub_secret_key: str
    stripe_rub_publishable_key: str

    postgres_db: str
    postgres_user: str
    postgres_password: str
    db_host: str
    db_port: int

    # class Config:
    #     env_file = '.env'

settings = Settings()