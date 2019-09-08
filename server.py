from abc import ABC, abstractmethod

class Server(ABC):
    @abstractmethod
    def __init__(self, HOST, PORT):
        pass

    @abstractmethod
    def run(self):
        pass