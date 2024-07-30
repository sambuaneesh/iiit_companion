import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# App settings
APP_NAME = "IIIT Companion"
DEBUG = os.getenv("DEBUG", "False") == "True"

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Generated app settings
MIN_PORT = 8000
MAX_PORT = 9000
GENERATED_APPS_DIR = os.path.join(BASE_DIR, "generated_apps")

# Ensure the generated apps directory exists
os.makedirs(GENERATED_APPS_DIR, exist_ok=True)
