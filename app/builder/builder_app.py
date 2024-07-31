import os
import streamlit as st
from app.utils.app_generator import AppGenerator
from app.config import APP_NAME, MICROSERVICES_DIR
from app.utils.logger import setup_logger

class BuilderApp:
    def __init__(self):
        self.logger = setup_logger('BuilderApp')
        self.keyword_tree = self._discover_services()
        self.all_keywords = self.flatten_keywords()
        self.app_generator = AppGenerator()

    def _discover_services(self):
        keyword_tree = {}
        for category in os.listdir(MICROSERVICES_DIR):
            category_path = os.path.join(MICROSERVICES_DIR, category)
            if os.path.isdir(category_path):
                keyword_tree[category] = [
                    os.path.splitext(service)[0]
                    for service in os.listdir(category_path)
                    if service.endswith('.py')
                ]
        return keyword_tree

    def flatten_keywords(self):
        return [topic for topic in self.keyword_tree.keys()] + \
               [keyword for keywords in self.keyword_tree.values() for keyword in keywords]

    def run(self):
        self.logger.info("Starting BuilderApp")
        st.title(f"{APP_NAME} Builder")

        st.write("Select the features you want in your personalized IIIT Companion app:")

        selected_keywords = st.multiselect("Select features:", self.all_keywords)

        if st.button("Create My IIIT Companion App"):
            if selected_keywords:
                processed_keywords = self.process_selected_keywords(selected_keywords)
                if processed_keywords:
                    app_url = self.app_generator.generate_app(processed_keywords)
                    st.success(f"Your personalized {APP_NAME} app has been created! Access it at: {app_url}")
                else:
                    st.error("No valid features selected. Please try again.")
            else:
                st.error("Please select at least one feature to create your app.")

    def process_selected_keywords(self, selected_keywords):
        self.logger.info(f"Processing selected keywords: {selected_keywords}")
        processed_keywords = {topic: [] for topic in self.keyword_tree}

        for keyword in selected_keywords:
            if keyword in self.keyword_tree:
                # If a main topic is selected, include all its features
                processed_keywords[keyword] = self.keyword_tree[keyword]
            else:
                # Check which topic the keyword belongs to
                for topic, features in self.keyword_tree.items():
                    if keyword in features:
                        processed_keywords[topic].append(keyword)

        self.logger.info(f"Processed keywords: {processed_keywords}")
        # Remove empty topics
        processed_keywords = {k: v for k, v in processed_keywords.items() if v}

        return processed_keywords
