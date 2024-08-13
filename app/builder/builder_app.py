import streamlit as st
from app.utils.app_generator import AppGenerator
from app.config import APP_NAME
from app.utils.logger import setup_logger
from chatbot import take_input

class BuilderApp:
    def __init__(self):
        self.keyword_tree = {
            "environmental": ["temperature", "humidity", "air quality"],
            "resource": ["library", "cafeteria", "study rooms"],
            "academic": ["assignments", "classes", "grades"],
            "event": ["campus events", "clubs", "workshops"],
            "health": ["wellness tips", "fitness", "mental health"]
        }
        self.all_keywords = self.flatten_keywords()
        self.app_generator = AppGenerator()
        self.logger = setup_logger('BuilderApp')

    def flatten_keywords(self):
        return [topic for topic in self.keyword_tree.keys()] + \
               [keyword for keywords in self.keyword_tree.values() for keyword in keywords]

    def run(self):
        self.logger.info("Starting BuilderApp")
        st.title(f"{APP_NAME} Builder")
        if 'conversation' not in st.session_state:
            st.session_state.conversation = []
        st.write("Your personalized IIIT Companion app:")

        user_input = st.text_input("Enter a sentence describing your desired app features:")
        if user_input:
            selected_keywords = take_input(user_input)
            # print(selected_keywords)
            # Convert the string to a list of keywords
            while selected_keywords is None:
                st.session_state.conversation.append(selected_keywords)
                selected_keywords = take_input(selected_keywords)
            self.logger.info(f"Selected Keywords: {selected_keywords}")
            st.write(f"Selected Keywords: {selected_keywords}")

        if st.button("Create My IIIT Companion App"):
            if selected_keywords:
                processed_keywords = self.process_selected_keywords(selected_keywords)
                if processed_keywords:
                    app_url = self.app_generator.generate_app(processed_keywords)
                    st.success(f"Your personalized {APP_NAME} app has been created! Access it at: {app_url}")
                else:
                    st.error("No valid features selected. Please try again.")
            else:
                st.error("Please enter a sentence to describe your desired features.")

    def process_selected_keywords(self, selected_keywords):
        self.logger.info(f"Processing selected keywords: {selected_keywords}")
        processed_keywords = {topic: [] for topic in self.keyword_tree}

        for keyword in selected_keywords:
            if keyword in self.keyword_tree:
                # If a main topic is selected, include all its features
                self.logger.info(f"Keyword '{keyword}' is a main topic")
                processed_keywords[keyword] = self.keyword_tree[keyword]
            else:
                # Check which topic the keyword belongs to
                for topic, features in self.keyword_tree.items():
                    if keyword in features:
                        self.logger.info(f"Keyword '{keyword}' belongs to topic '{topic}'")
                        processed_keywords[topic].append(keyword)

        self.logger.info(f"Processed keywords: {processed_keywords}")
        # Remove empty topics
        processed_keywords = {k: v for k, v in processed_keywords.items() if v}

        return processed_keywords

# Run the BuilderApp
if __name__ == "__main__":
    app = BuilderApp()
    app.run()
