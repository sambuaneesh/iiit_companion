import streamlit as st
from app.builder.keyword_manager import KeywordManager
from app.utils.app_generator import AppGenerator
from app.config import APP_NAME

class BuilderApp:
    def __init__(self):
        self.keyword_manager = KeywordManager()
        self.app_generator = AppGenerator()

    def run(self):
        st.title(f"{APP_NAME} Builder")

        st.write("Select the features you want in your personalized IIIT Companion app:")

        selected_keywords = {}
        for category, keywords in self.keyword_manager.get_keywords().items():
            st.subheader(category)
            selected_keywords[category] = st.multiselect(f"Select {category} features:", keywords)

        if st.button("Create My IIIT Companion App"):
            if any(selected_keywords.values()):
                app_url = self.app_generator.generate_app(selected_keywords)
                st.success(f"Your personalized {APP_NAME} app has been created! Access it at: {app_url}")
            else:
                st.error("Please select at least one feature to create your app.")
