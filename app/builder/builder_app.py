import streamlit as st
from app.utils.app_generator import AppGenerator
from app.config import APP_NAME

class BuilderApp:
    def __init__(self):
        self.keywords = {
            "Environmental": ["temperature", "humidity", "air quality"],
            "Resource": ["library", "cafeteria", "study rooms"],
            "Academic": ["assignments", "classes", "grades"],
            "Event": ["campus events", "clubs", "workshops"],
            "Health": ["wellness tips", "fitness", "mental health"]
        }
        self.app_generator = AppGenerator()

    def run(self):
        st.title(f"{APP_NAME} Builder")

        st.write("Select the features you want in your personalized IIIT Companion app:")

        selected_keywords = {}
        for category, keywords in self.keywords.items():
            st.subheader(category)
            selected_keywords[category] = st.multiselect(f"Select {category} features:", keywords)

        if st.button("Create My IIIT Companion App"):
            if any(selected_keywords.values()):
                app_url = self.app_generator.generate_app(selected_keywords)
                st.success(f"Your personalized {APP_NAME} app has been created! Access it at: {app_url}")
            else:
                st.error("Please select at least one feature to create your app.")
