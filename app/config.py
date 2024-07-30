import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# App settings
APP_NAME = "IIIT Companion"
DEBUG = os.getenv("DEBUG", "False") == "True"

# Microservice ports
ENVIRONMENTAL_PORT = 8001
RESOURCE_PORT = 8002
ACADEMIC_PORT = 8003
EVENT_PORT = 8004
HEALTH_PORT = 8005

# Builder app port
BUILDER_PORT = 8000

# Generated app settings
MIN_PORT = 9000
MAX_PORT = 9999
GENERATED_APPS_DIR = os.path.join(BASE_DIR, "generated_apps")

# Ensure the generated apps directory exists
os.makedirs(GENERATED_APPS_DIR, exist_ok=True)
