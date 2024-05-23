from EjercicioENUM.PriceStrategy import PriceStrategy


class TicketPriceCalculator:
    def __init__(self, strategy: PriceStrategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: PriceStrategy):
        self.strategy = strategy

    def calculateTicketPrice(self, base_price):
        if not self.strategy:
            raise ValueError("Strategy not set")
        return self.strategy.calculateTicketPrice(base_price)