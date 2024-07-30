from abc import ABC, abstractmethod

class MicroserviceBase(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def render(self, col):
        pass
