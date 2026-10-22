import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

    DATABASE_URL = os.environ.get("DATABASE_URL")

    if DATABASE_URL and DATABASE_URL.startswith("mysql://"):
        DATABASE_URL = DATABASE_URL.replace(
            "mysql://",
            "mysql+pymysql://",
            1
        )

    SQLALCHEMY_DATABASE_URI = DATABASE_URL

    SQLALCHEMY_TRACK_MODIFICATIONS = False