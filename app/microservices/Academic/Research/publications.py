from app.microservices.base import MicroserviceBase
from app.config import microservice_ports
import random


class PublicationsService(MicroserviceBase):
    def __init__(self):
        super().__init__(
            "Publications", microservice_ports["academic_research_publications"]
        )

        @self.app.get("/data")
        async def get_data():
            return self._get_publications()

    def _get_publications(self):
        publications = [
            {"title": "Advances in AI", "author": "Dr. Smith", "year": 2024},
            {
                "title": "Quantum Computing Breakthroughs",
                "author": "Dr. Johnson",
                "year": 2023,
            },
            {
                "title": "New Frontiers in Data Science",
                "author": "Dr. Williams",
                "year": 2024,
            },
        ]
        return {"recent_publications": random.sample(publications, k=2)}


def start_publications_service():
    service = PublicationsService()
    service.start()


if __name__ == "__main__":
    start_publications_service()
