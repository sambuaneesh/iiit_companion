import streamlit as st
import subprocess
import random
import os

# List of available microservices
MICROSERVICES = [
    "SensorDataCollectionService",
    "UserLocationService",
    "ResourceAvailabilityService",
    "NotificationService",
    "PersonalDashboardService"
]

def create_app(selected_services):
    # Generate a random port number between 8000 and 9000
    port = random.randint(8000, 9000)
    
    # Create a new directory for the application
    app_dir = f"iiit_companion_{port}"
    os.makedirs(app_dir, exist_ok=True)
    
    # Create the main application file
    with open(f"{app_dir}/app.py", "w") as f:
        f.write("import streamlit as st\n")
        f.write("from microservices import *\n")
        
        f.write("\nst.title('IIIT Companion')\n")
        
        for service in selected_services:
            f.write(f"\nst.header('{service}')\n")
            f.write(f"{service}().run()\n")
    
    # Copy microservices script to the new directory
    subprocess.run(["cp", "microservices.py", app_dir])
    
    # Run the new Streamlit app
    subprocess.Popen(["streamlit", "run", f"{app_dir}/app.py", "--server.port", str(port)])
    
    return f"http://localhost:{port}"

st.title("IIIT Companion Builder")

st.write("Select the microservices you want to include in your IIIT Companion:")

selected_services = st.multiselect("Available Microservices", MICROSERVICES)

if st.button("Build IIIT Companion"):
    if selected_services:
        app_url = create_app(selected_services)
        st.success(f"IIIT Companion created successfully! Access it at: {app_url}")
    else:
        st.error("Please select at least one microservice.")
