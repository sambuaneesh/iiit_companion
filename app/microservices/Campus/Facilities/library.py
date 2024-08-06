from app.microservices.base import MicroserviceBase
from app.config import microservice_ports
import random


class LibraryService(MicroserviceBase):
    def __init__(self):
        super().__init__("Library", microservice_ports["campus_facilities_library"])

        @self.app.get("/data")
        async def get_data():
            return self._get_library_info()

    def _get_library_info(self):
        books = [
            {"title": "Introduction to Algorithms", "available": True},
            {"title": "Design Patterns", "available": False},
            {"title": "Clean Code", "available": True},
        ]
        return {
            "open_hours": "8:00 AM - 10:00 PM",
            "available_books": random.sample(books, k=2),
        }


def start_library_service():
    service = LibraryService()
    service.start()


if __name__ == "__main__":
    start_library_service()
