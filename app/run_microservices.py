import os
import sys
import importlib
import threading
import time
import psutil

# Get the absolute path of the current file
current_file = os.path.abspath(__file__)

# Get the root directory of the project (one level up from the current file)
project_root = os.path.dirname(os.path.dirname(current_file))

# Add the project root to the Python path
sys.path.insert(0, project_root)

# Import the config module
import app.config as config

# Set up the configuration
config.set_paths(os.path.dirname(current_file))
config.setup()

# Now we can access the configuration variables
MICROSERVICES_DIR = config.MICROSERVICES_DIR
microservice_ports = config.microservice_ports

# Now import the logger
from app.utils.logger import setup_logger
from app.utils.port_manager import update_port_map, PORT_MAP_FILE, clean_port_map

logger = setup_logger("run_microservices")


def run_microservice(module_name, service_name, port):
    try:
        logger.info(f"Importing module {module_name} for {service_name}")
        module = importlib.import_module(module_name)

        logger.info(f"Getting start function for {service_name}")
        start_function = getattr(module, f"start_{service_name.lower()}_service")

        logger.info(f"Starting {service_name} service on port {port}")
        update_port_map(service_name.lower(), port)
        start_function()

    except ImportError as e:
        logger.error(
            f"Error importing module for {service_name}: {str(e)}", exc_info=True
        )
    except AttributeError as e:
        logger.error(
            f"Error finding start function for {service_name}: {str(e)}", exc_info=True
        )
    except Exception as e:
        logger.error(f"Error starting {service_name} service: {str(e)}", exc_info=True)


def run_all_microservices():
    # Clear the existing port map
    if os.path.exists(PORT_MAP_FILE):
        os.remove(PORT_MAP_FILE)

    threads = []
    for category in os.listdir(config.MICROSERVICES_DIR):
        category_path = os.path.join(config.MICROSERVICES_DIR, category)
        if os.path.isdir(category_path):
            for service in os.listdir(category_path):
                if service.endswith(".py") and not service.startswith("__"):
                    service_name = os.path.splitext(service)[0]
                    module_name = f"app.microservices.{category}.{service_name}"
                    port_key = f"{category.lower()}_{service_name.lower()}"
                    if port_key in config.microservice_ports:
                        port = config.microservice_ports[port_key]
                        logger.info(
                            f"Starting thread for {service_name} service on port {port}"
                        )
                        thread = threading.Thread(
                            target=run_microservice,
                            args=(module_name, service_name, port),
                        )
                        thread.start()
                        threads.append(thread)
                    else:
                        logger.error(f"Port not found for service: {port_key}")

    for thread in threads:
        thread.join()

    # Clean and standardize the port map after all services have started
    clean_port_map()


if __name__ == "__main__":
    logger.info("Starting all microservices...")
    run_all_microservices()
    logger.info("All microservices started")

    # Keep the script running and periodically log running services
    while True:
        time.sleep(60)  # Log every 60 seconds
        logger.info("Currently running microservices:")
        for process in psutil.process_iter(["pid", "name", "cmdline"]):
            if "python" in process.info[
                "name"
            ].lower() and "run_microservices.py" in " ".join(process.info["cmdline"]):
                logger.info(
                    f"PID: {process.info['pid']}, Command: {' '.join(process.info['cmdline'])}"
                )
