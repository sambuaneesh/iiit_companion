from app.microservices.base import MicroserviceBase
from app.config import RESOURCE_PORT
import random

class ResourceService(MicroserviceBase):
    def __init__(self):
        super().__init__("Resource", RESOURCE_PORT)

        @self.app.get("/data")
        async def get_data():
            return {
                "library_availability": self._get_library_availability(),
                "cafeteria_menu": self._get_cafeteria_menu(),
                "study_rooms": self._get_study_rooms()
            }

    def _get_library_availability(self):
        return f"{random.randint(0, 100)}%"

    def _get_cafeteria_menu(self):
        meals = ["Pasta", "Pizza", "Salad", "Burger", "Soup", "Sandwich", "Curry", "Stir Fry"]
        return random.sample(meals, 3)

    def _get_study_rooms(self):
        return f"{random.randint(1, 10)} rooms available"

def start_resource_service():
    service = ResourceService()
    service.start()
