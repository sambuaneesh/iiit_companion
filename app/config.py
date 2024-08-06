import os
from typing import Dict, Optional

APP_NAME: str = "IIIT Companion"
BUILDER_PORT: int = 8501
MIN_PORT: int = 9000
MAX_PORT: int = 9999

# These paths will be set dynamically when the config is loaded
APP_DIR: Optional[str] = None
MICROSERVICES_DIR: Optional[str] = None
GENERATED_APPS_DIR: Optional[str] = None

# Dynamically allocate ports for microservices
microservice_ports: Dict[str, int] = {}
current_port: int = MIN_PORT


def set_paths(base_path: str) -> None:
    global APP_DIR, MICROSERVICES_DIR, GENERATED_APPS_DIR
    APP_DIR = base_path
    MICROSERVICES_DIR = os.path.join(base_path, "microservices")
    GENERATED_APPS_DIR = os.path.join(base_path, "generated_apps")


def discover_microservices() -> None:
    global microservice_ports, current_port
    if MICROSERVICES_DIR is None:
        raise ValueError("MICROSERVICES_DIR is not set. Call set_paths() first.")
    for category in os.listdir(MICROSERVICES_DIR):
        category_path = os.path.join(MICROSERVICES_DIR, category)
        if os.path.isdir(category_path):
            for service in os.listdir(category_path):
                if service.endswith(".py") and not service.startswith("__"):
                    service_name = os.path.splitext(service)[0]
                    port_key = f"{category.lower()}_{service_name.lower()}"
                    microservice_ports[port_key] = current_port
                    current_port += 1


# This function will be called after setting the paths
def setup() -> None:
    if GENERATED_APPS_DIR is None:
        raise ValueError("GENERATED_APPS_DIR is not set. Call set_paths() first.")
    discover_microservices()
    os.makedirs(GENERATED_APPS_DIR, exist_ok=True)
