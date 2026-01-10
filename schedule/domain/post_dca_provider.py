from abc import ABC, abstractmethod

class PostDcaProvider(ABC):

    @abstractmethod
    def post(self, amount, symbol):
        """
        Make a request to purchase an asset
        """
        pass

    @abstractmethod
    def get_user_balances(self):
        """
        Retrieve user balances
        """
        pass