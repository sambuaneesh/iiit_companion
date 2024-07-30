from app.microservices.base import MicroserviceBase
from app.config import ACADEMIC_PORT
import random

class AcademicService(MicroserviceBase):
    def __init__(self):
        super().__init__("Academic", ACADEMIC_PORT)

        @self.app.get("/data")
        async def get_data():
            return {
                "assignments": self._get_assignments(),
                "classes": self._get_classes(),
                "grades": self._get_grades()
            }

    def _get_assignments(self):
        assignments = [
            "Math homework due in 2 days",
            "CS project due next week",
            "Physics lab report due tomorrow",
            "English essay due in 3 days",
            "History presentation next Monday"
        ]
        return random.sample(assignments, 2)

    def _get_classes(self):
        classes = [
            "9:00 AM - Math",
            "11:00 AM - Computer Science",
            "2:00 PM - Physics",
            "4:00 PM - English Literature",
            "6:00 PM - History"
        ]
        return random.sample(classes, 3)

    def _get_grades(self):
        subjects = ["Math", "Computer Science", "Physics", "English", "History"]
        return {subject: random.randint(60, 100) for subject in random.sample(subjects, 3)}

def start_academic_service():
    service = AcademicService()
    service.start()
