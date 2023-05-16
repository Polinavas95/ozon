from dotenv import find_dotenv
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    host: str = Field(None, env='HOST')
    client_id: str = Field(None, env='CLIENT_ID')
    api_key: str = Field(None, env='API_KEY')


settings = Settings(_env_file=find_dotenv(), _env_file_encoding='utf-8')
