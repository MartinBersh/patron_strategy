from enum import Enum, auto

class PriceStrategy(Enum):
    ADULT = auto()
    CHILD = auto()
    STUDENT = auto()

    def calculateTicketPrice(self, base_price):
        if self == PriceStrategy.ADULT:
            return base_price
        elif self == PriceStrategy.CHILD:
            return base_price - (base_price * 0.3)
        elif self == PriceStrategy.STUDENT:
            return base_price - (base_price * 0.5)
