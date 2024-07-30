# Microservices Documentation

This document provides detailed information about each microservice in the IIIT Companion application, including their purpose, API endpoints, and data structures.

## Base Microservice

All microservices inherit from the `MicroserviceBase` class defined in `app/microservices/base.py`. This base class provides common functionality for starting the FastAPI server.

## 1. Environmental Service

**File**: `app/microservices/environmental.py`
**Port**: 8001

### Purpose
Provides real-time environmental data for the campus.

### API Endpoints

#### GET /data
Returns environmental data.

**Response**:
```json
{
  "temperature": float,
  "humidity": float,
  "air_quality": {
    "value": int,
    "status": string
  }
}
```

## 2. Resource Service

**File**: `app/microservices/resource.py`
**Port**: 8002

### Purpose
Manages information about campus resources.

### API Endpoints

#### GET /data
Returns resource availability data.

**Response**:
```json
{
  "library_availability": string,
  "cafeteria_menu": list[string],
  "study_rooms": string
}
```

## 3. Academic Service

**File**: `app/microservices/academic.py`
**Port**: 8003

### Purpose
Handles academic-related information.

### API Endpoints

#### GET /data
Returns academic data.

**Response**:
```json
{
  "assignments": list[string],
  "classes": list[string],
  "grades": dict[string, int]
}
```

## 4. Event Service

**File**: `app/microservices/event.py`
**Port**: 8004

### Purpose
Manages campus events and activities.

### API Endpoints

#### GET /data
Returns event data.

**Response**:
```json
{
  "campus_events": list[string],
  "club_activities": list[string],
  "workshops": string
}
```

## 5. Health Service

**File**: `app/microservices/health.py`
**Port**: 8005

### Purpose
Provides health and wellness information.

### API Endpoints

#### GET /data
Returns health-related data.

**Response**:
```json
{
  "wellness_tip": string,
  "fitness_suggestion": string,
  "mental_health_resource": string
}
```

## Adding a New Microservice

To add a new microservice to the IIIT Companion application:

1. Create a new Python file in the `app/microservices/` directory.
2. Import and inherit from the `MicroserviceBase` class.
3. Implement the necessary API endpoints using FastAPI decorators.
4. Add a `start_*_service()` function to initialize and run the microservice.
5. Update the `app/config.py` file to include a new port number for your service.
6. Modify the `app/run_microservices.py` file to start your new service.
7. Update the `AppGenerator` class in `app/utils/app_generator.py` to include logic for your new service.
8. Add new options in the Builder Application (`app/builder/builder_app.py`) to allow users to select features from your new service.

## Best Practices

- Keep each microservice focused on a specific domain or functionality.
- Ensure proper error handling and input validation in your API endpoints.
- Use asynchronous programming (async/await) when dealing with I/O operations for better performance.
- Implement logging in each microservice for easier debugging and monitoring.
- Consider adding health check endpoints to each microservice for monitoring purposes.

## Future Improvements

- Implement authentication and authorization for microservice API endpoints.
- Add rate limiting to prevent abuse of the services.
- Implement caching mechanisms to reduce load on frequently accessed data.
- Create a service discovery mechanism for easier management of microservice endpoints.

This documentation provides an overview of the existing microservices and guidelines for extending the system with new services. As the application grows, maintain this document to reflect any changes or additions to the microservices architecture.
