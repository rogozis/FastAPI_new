from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    # Secrets
    gemini_api_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings = Settings()