GENERATED_APP_TEMPLATE = """
import streamlit as st
from app.microservices.environmental import EnvironmentalService
from app.microservices.resource import ResourceService
from app.microservices.academic import AcademicService
from app.microservices.event import EventService
from app.microservices.health import HealthService

st.set_page_config(page_title="My IIIT Companion", page_icon="🏫", layout="wide")

st.title("My IIIT Companion")

# Initialize services
environmental_service = EnvironmentalService()
resource_service = ResourceService()
academic_service = AcademicService()
event_service = EventService()
health_service = HealthService()

# Display selected features
{environmental}
{resource}
{academic}
{event}
{health}
"""
