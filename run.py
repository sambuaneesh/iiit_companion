import subprocess
import sys
from app.config import BUILDER_PORT

def run_microservices():
    subprocess.Popen([sys.executable, "app/run_microservices.py"])

def run_streamlit():
    subprocess.run([
        sys.executable, "-m", "streamlit", "run",
        "app/main.py",
        "--server.port", str(BUILDER_PORT)
    ])

if __name__ == "__main__":
    run_microservices()
    run_streamlit()
