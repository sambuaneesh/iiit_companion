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


def discover_microservices(directory=None, prefix=""):
    global microservice_ports, current_port
    if directory is None:
        if MICROSERVICES_DIR is None:
            raise ValueError("MICROSERVICES_DIR is not set. Call set_paths() first.")
        directory = MICROSERVICES_DIR

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            discover_microservices(item_path, f"{prefix}{item.lower()}_")
        elif item.endswith(".py") and not item.startswith("__"):
            service_name = os.path.splitext(item)[0]
            port_key = f"{prefix}{service_name.lower()}"
            microservice_ports[port_key] = current_port
            current_port += 1


def setup():
    if APP_DIR is None or MICROSERVICES_DIR is None or GENERATED_APPS_DIR is None:
        raise ValueError("Paths are not set. Call set_paths() first.")
    discover_microservices()
    os.makedirs(GENERATED_APPS_DIR, exist_ok=True)


def get_port(service_name: str) -> int:
    return microservice_ports.get(service_name.lower(), None)
