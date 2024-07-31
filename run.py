import os
import sys
import subprocess
import time
from app.config import BUILDER_PORT
from app.utils.logger import setup_logger

logger = setup_logger('run')

def run_microservices():
    logger.info("Starting microservices...")
    microservices_script = os.path.join(os.path.dirname(__file__), "app", "run_microservices.py")
    subprocess.Popen([sys.executable, microservices_script])

    # Give microservices time to start
    time.sleep(10)
    logger.info("Microservices should be running now")

def run_streamlit():
    logger.info(f"Starting Streamlit app on port {BUILDER_PORT}")
    main_script = os.path.join(os.path.dirname(__file__), "app", "main.py")
    subprocess.run([
        sys.executable, "-m", "streamlit", "run",
        main_script,
        "--server.port", str(BUILDER_PORT)
    ])

if __name__ == "__main__":
    run_microservices()
    run_streamlit()
