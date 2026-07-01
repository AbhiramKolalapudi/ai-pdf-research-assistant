from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    gemini_api_key: str

    embedding_model: str = "all-MiniLM-L6-v2"
    llm_model: str = "gemini-2.5-flash-lite"

    chroma_db_path: str = "chroma_db"

    upload_dir: str = "data/uploads"

    top_k: int = 5
    temperature: float = 0.2

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()