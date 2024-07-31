import streamlit as st
from app.utils.app_generator import AppGenerator
from app.config import APP_NAME

class BuilderApp:
    def __init__(self):
        self.keyword_tree = {
            "Environmental": ["temperature", "humidity", "air quality"],
            "Resource": ["library", "cafeteria", "study rooms"],
            "Academic": ["assignments", "classes", "grades"],
            "Event": ["campus events", "clubs", "workshops"],
            "Health": ["wellness tips", "fitness", "mental health"]
        }
        self.all_keywords = self.flatten_keywords()
        self.app_generator = AppGenerator()

    def flatten_keywords(self):
        return [topic for topic in self.keyword_tree.keys()] + \
               [keyword for keywords in self.keyword_tree.values() for keyword in keywords]

    def run(self):
        st.title(f"{APP_NAME} Builder")

        st.write("Select the features you want in your personalized IIIT Companion app:")
        st.write("You can select main topics or specific features. Selecting a topic will include all its features.")

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

        # Remove empty topics
        processed_keywords = {k: v for k, v in processed_keywords.items() if v}

        return processed_keywords
