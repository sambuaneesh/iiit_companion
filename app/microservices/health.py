from app.microservices.base import MicroserviceBase
from app.config import HEALTH_PORT
import random

class HealthService(MicroserviceBase):
    def __init__(self):
        super().__init__("Health", HEALTH_PORT)

        @self.app.get("/data")
        async def get_data():
            return {
                "wellness_tip": self._get_wellness_tip(),
                "fitness_suggestion": self._get_fitness_suggestion(),
                "mental_health_resource": self._get_mental_health_resource()
            }

    def _get_wellness_tip(self):
        tips = [
            "Remember to stay hydrated!",
            "Take a 5-minute break every hour of studying",
            "Don't forget to eat breakfast before class",
            "Aim for 7-9 hours of sleep each night",
            "Practice deep breathing to reduce stress"
        ]
        return random.choice(tips)

    def _get_fitness_suggestion(self):
        suggestions = [
            "Try a 20-minute jog around campus",
            "Join a yoga session at the gym",
            "Take the stairs instead of the elevator today",
            "Do a quick 10-minute workout between classes",
            "Go for a bike ride this evening"
        ]
        return random.choice(suggestions)

    def _get_mental_health_resource(self):
        resources = [
            "Counseling services available at Student Center",
            "Meditation app free for students: Calm",
            "Join the Mindfulness Club for stress relief techniques",
            "24/7 mental health hotline: 1-800-273-TALK",
            "Student support group meets every Wednesday at 5 PM"
        ]
        return random.choice(resources)

def start_health_service():
    service = HealthService()
    service.start()
