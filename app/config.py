import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# App settings
APP_NAME = "IIIT Companion"
DEBUG = os.getenv("DEBUG", "False") == "True"

BASE_MICROSERVICE_PORT = 9000
MICROSERVICES_DIR = os.path.join(os.path.dirname(__file__), 'microservices')
GENERATED_APPS_DIR = os.path.join(os.path.dirname(__file__), 'generated_apps')

# Dynamically allocate ports for microservices
microservice_ports = {}
current_port = BASE_MICROSERVICE_PORT

for category in os.listdir(MICROSERVICES_DIR):
    category_path = os.path.join(MICROSERVICES_DIR, category)
    if os.path.isdir(category_path):
        for service in os.listdir(category_path):
            if service.endswith('.py'):
                service_name = os.path.splitext(service)[0]
                microservice_ports[f"{category.lower()}_{service_name}"] = current_port
                current_port += 1

# TODO: use this to set the port for the builder app
# Builder app port
BUILDER_PORT = 8000

# Generated app settings
MIN_PORT = 9000
MAX_PORT = 9999

# Ensure the generated apps directory exists
os.makedirs(GENERATED_APPS_DIR, exist_ok=True)
