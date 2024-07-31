import os
import sys

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

import streamlit as st
from app.builder.builder_app import BuilderApp
from app.config import BUILDER_PORT, APP_NAME
from app.utils.logger import setup_logger

logger = setup_logger('main')

def run_builder_app():
    logger.info(f"Starting {APP_NAME} Builder on port {BUILDER_PORT}")
    st.set_page_config(page_title=f"{APP_NAME} Builder", page_icon="🏗️", layout="wide")
    builder_app = BuilderApp()
    builder_app.run()

if __name__ == "__main__":
    run_builder_app()
