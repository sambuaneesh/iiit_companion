import random
from app.microservices.base import MicroserviceBase

class EnvironmentalService(MicroserviceBase):
    def get_data(self):
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

    def render(self, col):
        data = self.get_data()
        col.metric("Temperature", f"{data['temperature']}°C")
        col.metric("Humidity", f"{data['humidity']}%")
        col.metric("Air Quality Index", data['air_quality']['value'], delta=data['air_quality']['status'])
