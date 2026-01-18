from abc import ABC, abstractmethod

class SignatureProvider(ABC):
    
    @abstractmethod
    def sign(self, payload: str) -> str:
        """
        Generate signature from the given payload
        """
        pass