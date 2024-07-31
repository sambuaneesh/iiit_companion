import os
import importlib
import threading
from app.config import MICROSERVICES_DIR
from app.utils.logger import setup_logger

logger = setup_logger('run_microservices')

def run_microservice(module_name, service_name):
    try:
        module = importlib.import_module(module_name)
        start_function = getattr(module, f"start_{service_name}_service")
        start_function()
    except Exception as e:
        logger.error(f"Error starting {service_name} service: {str(e)}")

def run_all_microservices():
    threads = []
    for category in os.listdir(MICROSERVICES_DIR):
        category_path = os.path.join(MICROSERVICES_DIR, category)
        if os.path.isdir(category_path):
            for service in os.listdir(category_path):
                if service.endswith('.py'):
                    service_name = os.path.splitext(service)[0]
                    module_name = f"app.microservices.{category}.{service_name}"
                    thread = threading.Thread(target=run_microservice, args=(module_name, service_name))
                    thread.start()
                    threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    run_all_microservices()
