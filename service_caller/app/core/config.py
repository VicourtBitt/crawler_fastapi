from pydantic import BaseSettings

class Settings(BaseSettings):
    project_name: str = "Service Caller Devnology"
    pproject_version: str = "1.0"

    class Config:
        env_file = ".env"


settings = Settings()