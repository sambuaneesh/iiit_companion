import os
import random
import subprocess
import app.config as config
from app.utils.logger import setup_logger

class AppGenerator:
    def __init__(self):
        self.logger = setup_logger('AppGenerator')

    def generate_app(self, selected_keywords):
        self.logger.info(f"Generating app with keywords: {selected_keywords}")

        if config.GENERATED_APPS_DIR is None:
            self.logger.error("GENERATED_APPS_DIR is None. Make sure config.set_paths() and config.setup() have been called.")
            raise ValueError("GENERATED_APPS_DIR is not set. Configuration may not have been initialized properly.")

        port = self._get_available_port()
        app_dir = os.path.join(config.GENERATED_APPS_DIR, f"app_{port}")
        os.makedirs(app_dir, exist_ok=True)

        app_content = self._generate_app_content(selected_keywords)
        app_file_path = os.path.join(app_dir, "app.py")

        with open(app_file_path, "w") as f:
            f.write(app_content)

        self._run_app(app_file_path, port)
        return f"http://localhost:{port}"

    def _get_available_port(self):
        return random.randint(config.MIN_PORT, config.MAX_PORT)

    def _generate_app_content(self, selected_keywords):
        content = """
import streamlit as st
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(page_title="My IIIT Companion", page_icon="🏫", layout="wide")

st.title("My IIIT Companion")

"""
        for category, services in selected_keywords.items():
            content += f"\nst.header('{category}')\n"
            for service in services:
                port_key = f"{category.lower()}_{service.lower()}"
                if port_key in config.microservice_ports:
                    port = config.microservice_ports[port_key]
                    content += f"""
try:
    logger.info(f"Attempting to connect to {service.capitalize()} service on port {port}")
    response = requests.get("http://localhost:{port}/data", timeout=5)
    response.raise_for_status()
    data = response.json()
    st.subheader('{service.capitalize()}')
    st.write(data)
    logger.info(f"Successfully connected to {service.capitalize()} service")
except requests.exceptions.ConnectionError as e:
    logger.error(f"Connection error for {service.capitalize()} service: {{e}}")
    st.error(f"Unable to connect to {service.capitalize()} service. Please ensure the service is running.")
except requests.exceptions.Timeout as e:
    logger.error(f"Timeout error for {service.capitalize()} service: {{e}}")
    st.error(f"Connection to {service.capitalize()} service timed out. The service might be overloaded or not responding.")
except requests.exceptions.RequestException as e:
    logger.error(f"Request error for {service.capitalize()} service: {{e}}")
    st.error(f"An error occurred while connecting to {service.capitalize()} service: {{str(e)}}")
"""
                else:
                    self.logger.error(f"Port not found for service: {port_key}")
                    content += f"\nst.error('Configuration error for {service.capitalize()} service.')\n"

            return content

    def _run_app(self, app_file_path, port):
        self.logger.info(f"Running app at {app_file_path} on port {port}")
        subprocess.Popen(["streamlit", "run", app_file_path, "--server.port", str(port)])
