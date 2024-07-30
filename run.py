import subprocess
import sys

def run_microservices():
    subprocess.Popen([sys.executable, "app/run_microservices.py"])

def run_streamlit():
    subprocess.run(["streamlit", "run", "app/main.py"])

if __name__ == "__main__":
    run_microservices()
    run_streamlit()
