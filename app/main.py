import streamlit as st
from app.builder.builder_app import BuilderApp
from app.utils.logger import setup_logger

def run_builder_app():
    setup_logger()
    st.set_page_config(page_title="IIIT Companion Builder", page_icon="🏗️", layout="wide")
    builder_app = BuilderApp()
    builder_app.run()

if __name__ == "__main__":
    run_builder_app()
