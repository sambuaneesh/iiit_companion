# Customization Guide

This guide provides information on how to customize and extend the IIIT Companion application. Whether you want to add new features, modify existing ones, or change the appearance of the app, this document will help you navigate the customization process.

## Table of Contents

1. [Modifying Existing Microservices](#modifying-existing-microservices)
2. [Adding New Microservices](#adding-new-microservices)
3. [Customizing the Builder Application](#customizing-the-builder-application)
4. [Modifying Generated Dashboards](#modifying-generated-dashboards)
5. [Changing the Application Theme](#changing-the-application-theme)
6. [Adding Authentication](#adding-authentication)
7. [Integrating External APIs](#integrating-external-apis)
8. [Customizing Configuration](#customizing-configuration)
9. [Extending the App Generator](#extending-the-app-generator)

## Modifying Existing Microservices

To modify an existing microservice:

1. Navigate to the appropriate file in the `app/microservices/` directory.
2. Update the `get_data()` method to return the desired data structure.
3. If adding new endpoints, use FastAPI decorators to define them.

Example of modifying the Environmental Service:

```python
from app.microservices.base import MicroserviceBase
from app.config import ENVIRONMENTAL_PORT
import random

class EnvironmentalService(MicroserviceBase):
    def __init__(self):
        super().__init__("Environmental", ENVIRONMENTAL_PORT)

        @self.app.get("/data")
        async def get_data():
            return {
                "temperature": round(random.uniform(20, 30), 1),
                "humidity": round(random.uniform(30, 70), 1),
                "air_quality": self._get_air_quality(),
                "wind_speed": round(random.uniform(0, 20), 1)  # New field
            }

    # ... rest of the code
```

Remember to update the `AppGenerator` class and the Builder Application to accommodate any changes in the data structure.

## Adding New Microservices

To add a new microservice:

1. Create a new Python file in the `app/microservices/` directory (e.g., `new_service.py`).
2. Define a new class that inherits from `MicroserviceBase`.
3. Implement the necessary endpoints and logic.
4. Update `app/config.py` to include a new port for your service.
5. Modify `app/run_microservices.py` to start your new service.
6. Update the `AppGenerator` class in `app/utils/app_generator.py`.
7. Add new options in the Builder Application (`app/builder/builder_app.py`).

Example of a new microservice:

```python
# app/microservices/transportation.py
from app.microservices.base import MicroserviceBase
from app.config import TRANSPORTATION_PORT
import random

class TransportationService(MicroserviceBase):
    def __init__(self):
        super().__init__("Transportation", TRANSPORTATION_PORT)

        @self.app.get("/data")
        async def get_data():
            return {
                "bus_schedule": self._get_bus_schedule(),
                "bike_availability": self._get_bike_availability()
            }

    def _get_bus_schedule(self):
        # Implementation
        pass

    def _get_bike_availability(self):
        # Implementation
        pass

def start_transportation_service():
    service = TransportationService()
    service.start()
```

## Customizing the Builder Application

To customize the Builder Application:

1. Open `app/builder/builder_app.py`.
2. Modify the `BuilderApp` class to add or remove features.
3. Update the UI layout or add new Streamlit components as needed.

Example of adding a new category:

```python
class BuilderApp:
    def __init__(self):
        self.keywords = {
            # ... existing categories
            "Transportation": ["bus schedule", "bike sharing"]
        }
        # ... rest of the code

    def run(self):
        # ... existing code
        if "Transportation" in selected_keywords:
            content += self._get_transportation_content(selected_keywords["Transportation"])
        # ... rest of the code
```

## Modifying Generated Dashboards

To change the layout or content of generated dashboards:

1. Open `app/utils/app_generator.py`.
2. Modify the `_generate_app_content` method to change the overall structure.
3. Update individual content generation methods (e.g., `_get_environmental_content`) to modify specific sections.

Example of modifying the environmental content:

```python
def _get_environmental_content(self, keywords):
    content = """
st.header("Campus Environment")
env_data = requests.get("http://localhost:8001/data").json()
col1, col2, col3, col4 = st.columns(4)
"""
    if "temperature" in keywords:
        content += 'col1.metric("Temperature", f"{env_data["temperature"]}°C")\n'
    if "humidity" in keywords:
        content += 'col2.metric("Humidity", f"{env_data["humidity"]}%")\n'
    if "air quality" in keywords:
        content += 'col3.metric("Air Quality Index", env_data["air_quality"]["value"], delta=env_data["air_quality"]["status"])\n'
    if "wind speed" in keywords:
        content += 'col4.metric("Wind Speed", f"{env_data["wind_speed"]} km/h")\n'
    return content
```

## Changing the Application Theme

To change the application theme:

1. Create a custom theme file (e.g., `app/utils/custom_theme.py`).
2. Define your custom theme using Streamlit's theming options.
3. Update `app/main.py` and the app generator to use the custom theme.

Example of a custom theme:

```python
# app/utils/custom_theme.py
import streamlit as st

def set_custom_theme():
    st.set_page_config(
        page_title="IIIT Companion",
        page_icon="🏫",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown("""
        <style>
        .reportview-container {
            background: #f0f2f6
        }
        .sidebar .sidebar-content {
            background: #262730
        }
        </style>
    """, unsafe_allow_html=True)
```

Update `app/main.py`:

```python
from app.utils.custom_theme import set_custom_theme

def run_builder_app():
    set_custom_theme()
    builder_app = BuilderApp()
    builder_app.run()
```

## Adding Authentication

To add authentication:

1. Install a authentication library (e.g., `pip install streamlit-authenticator`).
2. Create an authentication module (e.g., `app/utils/auth.py`).
3. Implement authentication logic.
4. Update `app/main.py` and generated apps to use authentication.

Example of basic authentication:

```python
# app/utils/auth.py
import streamlit as st
import streamlit_authenticator as stauth

def authenticate():
    names = ["John Doe", "Jane Doe"]
    usernames = ["jdoe", "janedoe"]
    passwords = ["xxx", "xxx"]

    hashed_passwords = stauth.Hasher(passwords).generate()

    authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
        "iiit_companion", "abcdef", cookie_expiry_days=30)

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status:
        st.write(f'Welcome *{name}*')
        return True
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

    return False

# In app/main.py
from app.utils.auth import authenticate

def run_builder_app():
    if authenticate():
        builder_app = BuilderApp()
        builder_app.run()
```

## Integrating External APIs

To integrate external APIs:

1. Install necessary libraries (e.g., `pip install requests`).
2. Create a new module for API integration (e.g., `app/utils/external_api.py`).
3. Implement API calls and data processing.
4. Update relevant microservices or the app generator to use the external data.

Example of integrating a weather API:

```python
# app/utils/external_api.py
import requests

def get_weather_data(city):
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
    else:
        return None

# Update environmental_service.py
from app.utils.external_api import get_weather_data

class EnvironmentalService(MicroserviceBase):
    def __init__(self):
        super().__init__("Environmental", ENVIRONMENTAL_PORT)

        @self.app.get("/data")
        async def get_data():
            weather_data = get_weather_data("Your City")
            return {
                "temperature": weather_data["temperature"],
                "humidity": weather_data["humidity"],
                "description": weather_data["description"],
                "air_quality": self._get_air_quality()
            }
```

## Customizing Configuration

To customize the application configuration:

1. Open `app/config.py`.
2. Modify existing parameters or add new ones as needed.
3. Use environment variables for sensitive information.

Example of extended configuration:

```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# App settings
APP_NAME = os.getenv("APP_NAME", "IIIT Companion")
DEBUG = os.getenv("DEBUG", "False") == "True"

# Microservice ports
ENVIRONMENTAL_PORT = int(os.getenv("ENVIRONMENTAL_PORT", 8001))
RESOURCE_PORT = int(os.getenv("RESOURCE_PORT", 8002))
ACADEMIC_PORT = int(os.getenv("ACADEMIC_PORT", 8003))
EVENT_PORT = int(os.getenv("EVENT_PORT", 8004))
HEALTH_PORT = int(os.getenv("HEALTH_PORT", 8005))
TRANSPORTATION_PORT = int(os.getenv("TRANSPORTATION_PORT", 8006))

# Builder app port
BUILDER_PORT = int(os.getenv("BUILDER_PORT", 8000))

# Generated app settings
MIN_PORT = int(os.getenv("MIN_PORT", 9000))
MAX_PORT = int(os.getenv("MAX_PORT", 9999))
GENERATED_APPS_DIR = os.getenv("GENERATED_APPS_DIR", os.path.join(BASE_DIR, "generated_apps"))

# External API settings
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_CITY = os.getenv("WEATHER_API_CITY", "Your City")

# Ensure the generated apps directory exists
os.makedirs(GENERATED_APPS_DIR, exist_ok=True)
```

## Extending the App Generator

To extend the App Generator with new features:

1. Open `app/utils/app_generator.py`.
2. Add new methods for generating content for new features.
3. Update the `_generate_app_content` method to include the new features.

Example of adding transportation content:

```python
class AppGenerator:
    # ... existing code

    def _generate_app_content(self, selected_keywords):
        content = """
import streamlit as st
import requests

st.set_page_config(page_title="My IIIT Companion", page_icon="🏫", layout="wide")

st.title("My IIIT Companion")

"""
        # ... existing content generation

        if selected_keywords["Transportation"]:
            content += self._get_transportation_content(selected_keywords["Transportation"])

        return content

    def _get_transportation_content(self, keywords):
        content = """
st.header("Campus Transportation")
transport_data = requests.get("http://localhost:8006/data").json()
col1, col2 = st.columns(2)
"""
        if "bus schedule" in keywords:
            content += """
col1.subheader("Bus Schedule")
for bus in transport_data["bus_schedule"]:
    col1.write(f"Bus {bus['number']}: {bus['time']}")
"""
        if "bike sharing" in keywords:
            content += """
col2.subheader("Bike Availability")
col2.metric("Available Bikes", transport_data["bike_availability"])
"""
        return content

    # ... rest of the code
```

By following these customization guidelines, you can extend and modify the IIIT Companion application to suit your specific needs. Remember to test your changes thoroughly and update the documentation as you add new features or modify existing ones.
