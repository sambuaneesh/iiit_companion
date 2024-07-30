from fastapi import FastAPI
import uvicorn

class MicroserviceBase:
    def __init__(self, name: str, port: int):
        self.app = FastAPI()
        self.name = name
        self.port = port

    def start(self):
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)
