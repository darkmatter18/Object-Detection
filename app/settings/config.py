import os

from app.utils import get_env

class Settings:
    # Basic Application Information
    APP_TITLE = "AgWise App"
    PROJECT_NAME = "AgWise App Frontend Service"
    APP_DESCRIPTION = "AgWise App Frontend Service. Maintained by AgWise"
    CONTACT = {
        "name": "Arkadip Bhattacharya",
        "email": "arkadip.bhattacharya@nimblework.com",
    }

    DEBUG = not (os.getenv("ENV") == "PROD")
    LOCAL = not (os.getenv("ENV") == "PROD" or os.getenv("ENV") == "TEST")

    ROOT_PATH = "" if LOCAL else "/app"

    # Directory information
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
    LOGS_ROOT = os.path.join(PROJECT_ROOT, "logs")

    env = get_env(LOCAL, PROJECT_ROOT)

    # Route Information
    API_V1_STR = "/v1"

    CORS_ORIGINS = []  # noqa
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_METHODS = ["*"]
    CORS_ALLOW_HEADERS = ["*"]


settings = Settings()
