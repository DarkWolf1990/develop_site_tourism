import os
from dotenv import load_dotenv
from pathlib import Path

# Загружаем переменные из .env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

"""Конфигурация приложения"""
class Config:


    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "fallback-secret-key")

    class Database:
        """Настройки базы данных"""
        ENGINE: str = "django.db.backends.postgresql"
        NAME: str = os.getenv("DB_NAME", "default_db")
        USER: str = os.getenv("DB_USER", "default_user")
        PASSWORD: str = os.getenv("DB_PASS", "default_password")
        HOST: str = os.getenv("DB_HOST", "localhost")
        PORT: str = os.getenv("DB_PORT", "5432")


config = Config()  # Создаем объект конфигурации
