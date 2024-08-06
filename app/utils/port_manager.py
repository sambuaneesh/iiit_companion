import json
import os
import logging

PORT_MAP_FILE = "service_ports.json"


def update_port_map(service_name, port):
    try:
        if os.path.exists(PORT_MAP_FILE):
            with open(PORT_MAP_FILE, "r") as f:
                port_map = json.load(f)
        else:
            port_map = {}

        # Ensure service_name is lowercase
        service_name = service_name.lower()
        port_map[service_name] = port

        with open(PORT_MAP_FILE, "w") as f:
            json.dump(port_map, f, indent=2)

        logging.info(f"Updated port map: {service_name} -> {port}")
    except Exception as e:
        logging.error(f"Error updating port map: {e}")


def get_port(service_name):
    try:
        with open(PORT_MAP_FILE, "r") as f:
            port_map = json.load(f)
        # Ensure service_name is lowercase when searching
        return port_map.get(service_name.lower())
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON in port map file: {e}")
        return None
    except Exception as e:
        logging.error(f"Error reading port map: {e}")
        return None


def clean_port_map():
    try:
        if os.path.exists(PORT_MAP_FILE):
            with open(PORT_MAP_FILE, "r") as f:
                port_map = json.load(f)

            # Convert all keys to lowercase and remove duplicates
            cleaned_map = {k.lower(): v for k, v in port_map.items()}

            with open(PORT_MAP_FILE, "w") as f:
                json.dump(cleaned_map, f, indent=2)

            logging.info("Cleaned and standardized port map")
    except Exception as e:
        logging.error(f"Error cleaning port map: {e}")
