import os
import random
import subprocess
from app.config import MIN_PORT, MAX_PORT, GENERATED_APPS_DIR
from app.utils.logger import setup_logger

class AppGenerator:
    def __init__(self):
            self.logger = setup_logger('AppGenerator')

    def generate_app(self, selected_keywords):
        self.logger.info(f"Generating app with keywords: {selected_keywords}")
        port = self._get_available_port()
        app_dir = os.path.join(GENERATED_APPS_DIR, f"app_{port}")
        os.makedirs(app_dir, exist_ok=True)

        app_content = self._generate_app_content(selected_keywords)
        app_file_path = os.path.join(app_dir, "app.py")

        with open(app_file_path, "w" , encoding='utf-8') as f:
            f.write(app_content)

        self._run_app(app_file_path, port)
        self.logger.info(f"Generated app at: {app_file_path}")
        return f"http://localhost:{port}"

    def _get_available_port(self):
        return random.randint(MIN_PORT, MAX_PORT)

    def _generate_app_content(self, selected_keywords):
        content = """
import streamlit as st
import requests

st.set_page_config(page_title="My IIIT Companion", page_icon="🏫", layout="wide")

st.title("My IIIT Companion")

"""
        for topic, keywords in selected_keywords.items():
            if topic == "environmental":
                content += self._get_environmental_content(keywords)
            elif topic == "resource":
                content += self._get_resource_content(keywords)
            elif topic == "academic":
                content += self._get_academic_content(keywords)
            elif topic == "event":
                content += self._get_event_content(keywords)
            elif topic == "health":
                content += self._get_health_content(keywords)

        return content

    def _run_app(self, app_file_path, port):
        self.logger.info(f"Running app at port {port}")
        import subprocess
        subprocess.Popen(["streamlit", "run", app_file_path, "--server.port", str(port)])

    def _get_environmental_content(self, keywords):
        content = """
st.header("Campus Environment")
env_data = requests.get("http://localhost:8001/data").json()
col1, col2, col3 = st.columns(3)
"""
        if "temperature" in keywords:
            content += 'col1.metric("Temperature", f"{env_data["temperature"]}°C")\n'
        if "humidity" in keywords:
            content += 'col2.metric("Humidity", f"{env_data["humidity"]}%")\n'
        if "air quality" in keywords:
            content += 'col3.metric("Air Quality Index", env_data["air_quality"]["value"], delta=env_data["air_quality"]["status"])\n'
        return content

    def _get_resource_content(self, keywords):
        content = """
st.header("Campus Resources")
resource_data = requests.get("http://localhost:8002/data").json()
col1, col2, col3 = st.columns(3)
"""
        if "library" in keywords:
            content += 'col1.metric("Library Availability", resource_data["library_availability"])\n'
        if "cafeteria" in keywords:
            content += 'col2.write("Today\'s Cafeteria Menu:")\n'
            content += 'col2.write(", ".join(resource_data["cafeteria_menu"]))\n'
        if "study rooms" in keywords:
            content += 'col3.metric("Study Rooms", resource_data["study_rooms"])\n'
        return content

    def _get_academic_content(self, keywords):
        content = """
st.header("Academic Information")
academic_data = requests.get("http://localhost:8003/data").json()
col1, col2, col3 = st.columns(3)
"""
        if "assignments" in keywords:
            content += """
col1.subheader("Upcoming Assignments")
for assignment in academic_data["assignments"]:
    col1.write(f"- {assignment}")
"""
        if "classes" in keywords:
            content += """
col2.subheader("Class Schedule")
for class_ in academic_data["classes"]:
    col2.write(f"- {class_}")
"""
        if "grades" in keywords:
            content += """
col3.subheader("Recent Grades")
for subject, grade in academic_data["grades"].items():
    col3.write(f"{subject}: {grade}")
"""
        return content

    def _get_event_content(self, keywords):
        content = """
st.header("Campus Life")
event_data = requests.get("http://localhost:8004/data").json()
col1, col2, col3 = st.columns(3)
"""
        if "campus events" in keywords:
            content += """
col1.subheader("Upcoming Events")
for event in event_data["campus_events"]:
    col1.info(event)
"""
        if "clubs" in keywords:
            content += """
col2.subheader("Club Activities")
for activity in event_data["club_activities"]:
    col2.info(activity)
"""
        if "workshops" in keywords:
            content += """
col3.subheader("Workshops")
col3.info(event_data["workshops"])
"""
        return content

    def _get_health_content(self, keywords):
        content = """
st.header("Health & Wellness")
health_data = requests.get("http://localhost:8005/data").json()
col1, col2, col3 = st.columns(3)
"""
        if "wellness tips" in keywords:
            content += 'col1.success(f"Wellness Tip: {health_data["wellness_tip"]}")\n'
        if "fitness" in keywords:
            content += 'col2.success(f"Fitness Suggestion: {health_data["fitness_suggestion"]}")\n'
        if "mental health" in keywords:
            content += 'col3.success(f"Mental Health Resource: {health_data["mental_health_resource"]}")\n'
        return content
