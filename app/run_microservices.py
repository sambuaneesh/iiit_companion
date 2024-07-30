import os
import sys
import threading

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from app.microservices.environmental import start_environmental_service
from app.microservices.resource import start_resource_service
from app.microservices.academic import start_academic_service
from app.microservices.event import start_event_service
from app.microservices.health import start_health_service

def run_microservices():
    services = [
        start_environmental_service,
        start_resource_service,
        start_academic_service,
        start_event_service,
        start_health_service
    ]

    threads = []
    for service in services:
        thread = threading.Thread(target=service)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    run_microservices()
