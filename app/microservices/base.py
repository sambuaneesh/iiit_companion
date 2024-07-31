from fastapi import FastAPI
import uvicorn
from app.utils.logger import setup_logger

class MicroserviceBase:
    def __init__(self, name: str, port: int):
        self.app = FastAPI()
        self.name = name
        self.port = port
        self.logger = setup_logger(f"Microservice-{name}")

    def start(self):
        self.logger.info(f"Starting {self.name} microservice on port {self.port}")
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)
