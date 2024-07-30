# Architecture Overview

The IIIT Companion application is built using a microservices architecture, which allows for modularity, scalability, and ease of maintenance. This document provides an overview of the system architecture and how different components interact with each other.

## High-Level Architecture

The IIIT Companion system consists of the following main components:

1. Builder Application
2. Microservices
3. Generated User Dashboards

### Builder Application

- Implemented using Streamlit
- Allows users to select features for their personalized dashboard
- Generates new Streamlit apps based on user selections

### Microservices

- Implemented using FastAPI
- Each microservice runs independently on its own port
- Provides specific functionality and data for different features

### Generated User Dashboards

- Streamlit apps created dynamically based on user selections
- Fetch data from relevant microservices to display information

## Component Breakdown

### 1. Builder Application (`app/main.py` and `app/builder/builder_app.py`)

- Presents a user interface for selecting dashboard features
- Uses the `AppGenerator` class to create personalized dashboards

### 2. Microservices

- **Environmental Service** (`app/microservices/environmental.py`)
  - Provides temperature, humidity, and air quality data

- **Resource Service** (`app/microservices/resource.py`)
  - Manages library availability, cafeteria menu, and study room information

- **Academic Service** (`app/microservices/academic.py`)
  - Handles assignments, class schedules, and grades

- **Event Service** (`app/microservices/event.py`)
  - Manages campus events, club activities, and workshops

- **Health Service** (`app/microservices/health.py`)
  - Provides wellness tips, fitness suggestions, and mental health resources

### 3. App Generator (`app/utils/app_generator.py`)

- Creates new Streamlit apps based on user-selected features
- Generates Python code for personalized dashboards
- Launches the generated apps on available ports

### 4. Configuration (`app/config.py`)

- Centralized configuration for the entire application
- Defines port numbers, app settings, and other parameters

### 5. Main Runner (`run.py`)

- Entry point for the entire application
- Starts all microservices and launches the builder application

## Data Flow

1. User interacts with the Builder Application to select features
2. Builder Application uses AppGenerator to create a new dashboard
3. Generated dashboard fetches data from relevant microservices
4. Microservices provide data through their respective API endpoints
5. Dashboard displays the fetched data to the user

## Communication Between Components

- Builder Application to AppGenerator: Direct method calls
- AppGenerator to Microservices: HTTP requests (when generating app code)
- Generated Dashboards to Microservices: HTTP requests
- Microservices: Independent, no direct communication between them

## Scalability and Extensibility

The microservices architecture allows for:

- Easy addition of new features by creating new microservices
- Independent scaling of individual services based on demand
- Flexibility in technology choices for each microservice

## Security Considerations

- In the current implementation, all services and generated dashboards are accessible without authentication
- For production use, consider implementing authentication and authorization mechanisms
- Ensure proper network security and firewall rules are in place

## Future Improvements

- Implement a service discovery mechanism for dynamic service resolution
- Add a caching layer to reduce load on microservices
- Implement monitoring and logging for better observability
- Containerize microservices for easier deployment and scaling

This architecture provides a solid foundation for the IIIT Companion application, allowing for easy expansion and maintenance as the system grows and evolves.
