from app.microservices.base import MicroserviceBase
from app.config import ENVIRONMENTAL_PORT
import random


class EnvironmentalService(MicroserviceBase):
    def __init__(self):
        super().__init__("Environmental", ENVIRONMENTAL_PORT)

        @self.app.get("/data")
        async def get_data():
            return {
                "temperature": round(random.uniform(20, 30), 1),
                "humidity": round(random.uniform(30, 70), 1),
                "air_quality": self._get_air_quality()
            }

    def _get_air_quality(self):
        aqi = random.randint(0, 500)
        if aqi <= 50:
            status = "Good"
        elif aqi <= 100:
            status = "Moderate"
        elif aqi <= 150:
            status = "Unhealthy for Sensitive Groups"
        elif aqi <= 200:
            status = "Unhealthy"
        elif aqi <= 300:
            status = "Very Unhealthy"
        else:
            status = "Hazardous"
        return {"value": aqi, "status": status}

def start_environmental_service():
    service = EnvironmentalService()
    service.start()
