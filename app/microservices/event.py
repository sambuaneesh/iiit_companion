from app.microservices.base import MicroserviceBase
from app.config import EVENT_PORT
import random

class EventService(MicroserviceBase):
    def __init__(self):
        super().__init__("Event", EVENT_PORT)

        @self.app.get("/data")
        async def get_data():
            return {
                "campus_events": self._get_campus_events(),
                "club_activities": self._get_club_activities(),
                "workshops": self._get_workshops()
            }

    def _get_campus_events(self):
        events = [
            "Tech Talk at 4 PM in Lecture Hall",
            "Music Festival this weekend",
            "Career Fair next Tuesday",
            "Sports Day on Saturday",
            "Art Exhibition in the Student Center"
        ]
        return random.sample(events, 2)

    def _get_club_activities(self):
        activities = [
            "Coding Club: Hackathon next month",
            "Drama Club: Auditions this Friday",
            "Debate Club: Weekly meeting on Thursday",
            "Photography Club: Photo walk on Sunday",
            "Robotics Club: Robot building workshop"
        ]
        return random.sample(activities, 2)

    def _get_workshops(self):
        workshops = [
            "Resume Building Workshop next Tuesday",
            "Machine Learning Workshop this weekend",
            "Public Speaking Workshop on Wednesday",
            "Financial Literacy Seminar next month",
            "Design Thinking Workshop on Friday"
        ]
        return random.choice(workshops)

def start_event_service():
    service = EventService()
    service.start()
