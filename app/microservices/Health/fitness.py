from app.microservices.base import MicroserviceBase
from app.config import microservice_ports
import random

class FitnessService(MicroserviceBase):
    def __init__(self):
        super().__init__("Fitness", microservice_ports['health_fitness'])

        @self.app.get("/data")
        async def get_data():
            return self._get_fitness_suggestion()

    def _get_fitness_suggestion(self):
        suggestions = [
            "Try a 20-minute jog around campus",
            "Join a yoga session at the gym",
            "Take the stairs instead of the elevator today",
            "Do a quick 10-minute workout between classes",
            "Go for a bike ride this evening"
        ]
        return {"fitness_suggestion": random.choice(suggestions)}

def start_fitness_service():
    service = FitnessService()
    service.start()

if __name__ == "__main__":
    start_fitness_service()
