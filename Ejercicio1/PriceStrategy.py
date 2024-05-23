from abc import abstractmethod, ABC


class PriceStrategy(ABC):
 @abstractmethod
 def calculate_price(self, base_price: int) -> float: pass
