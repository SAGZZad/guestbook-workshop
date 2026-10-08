from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    database_url: str
    greeting: str = "Добро пожаловать в гостевую книгу!"


settings = Settings()