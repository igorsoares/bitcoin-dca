from abc import ABC, abstractmethod

class ExchangeSettings(ABC):

    @abstractmethod
    def settings(self, path:str):
        pass