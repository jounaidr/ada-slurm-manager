from pathlib import Path

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Model class for config options validation"""

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    asm_api_workers: int
    asm_api_version: str
    asm_api_port: int

    slurm_api_url: AnyHttpUrl
    slurm_api_verify_ssl: bool


def load_config() -> Config:
    """Load and validate config"""
    return Config()