from Ejercicio1.PriceStrategy import PriceStrategy


class TicketPriceCalculator:
 def __init__(self, strategy: PriceStrategy): self._strategy = strategy
 def set_strategy(self, strategy: PriceStrategy): self._strategy = strategy
 def calculate(self, base_price: int) -> float: return self._strategy.calculate_price(base_price)