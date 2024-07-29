import streamlit as st
import subprocess
import random
import os

# SensorDataCollectionService
class SensorDataCollectionService:
    def __init__(self):
        self.sensors = ["AirQuality", "Temperature", "Humidity", "Occupancy"]
    
    def collect_data(self):
        # Simulated data collection
        return {sensor: random.randint(0, 100) for sensor in self.sensors}
    
    def run(self):
        st.subheader("Sensor Data Collection")
        data = self.collect_data()
        for sensor, value in data.items():
            st.write(f"{sensor}: {value}")

# UserLocationService
class UserLocationService:
    def __init__(self):
        self.locations = ["Library", "Cafeteria", "Classroom", "Hostel", "Sports Complex"]
    
    def get_user_location(self):
        return random.choice(self.locations)
    
    def run(self):
        st.subheader("User Location")
        location = self.get_user_location()
        st.write(f"Current location: {location}")

# ResourceAvailabilityService
class ResourceAvailabilityService:
    def __init__(self):
        self.resources = {
            "Study Rooms": 10,
            "Library Seats": 50,
            "Computer Labs": 3
        }
    
    def check_availability(self):
        return {resource: random.randint(0, count) for resource, count in self.resources.items()}
    
    def run(self):
        st.subheader("Resource Availability")
        availability = self.check_availability()
        for resource, available in availability.items():
            st.write(f"{resource}: {available}/{self.resources[resource]} available")

# NotificationService
class NotificationService:
    def __init__(self):
        self.notifications = [
            "Air quality alert: Poor air quality detected outdoors",
            "Resource available: Study room 3 is now free",
            "Event reminder: Guest lecture in 30 minutes",
            "Health tip: Take a break and stretch"
        ]
    
    def get_notification(self):
        return random.choice(self.notifications)
    
    def run(self):
        st.subheader("Notifications")
        st.write(self.get_notification())

# PersonalDashboardService
class PersonalDashboardService:
    def __init__(self):
        self.user_data = {
            "Name": "John Doe",
            "Course": "Computer Science",
            "Year": 3,
            "GPA": 3.8,
            "Upcoming Deadlines": ["AI Project: 3 days", "Database Quiz: 1 week"]
        }
    
    def generate_dashboard(self):
        return self.user_data
    
    def run(self):
        st.subheader("Personal Dashboard")
        dashboard = self.generate_dashboard()
        for key, value in dashboard.items():
            if isinstance(value, list):
                st.write(f"{key}:")
                for item in value:
                    st.write(f"- {item}")
            else:
                st.write(f"{key}: {value}")
