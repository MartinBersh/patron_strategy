from EjercicioENUM.PriceStrategy import PriceStrategy
from EjercicioENUM.TicketPriceCalculator import TicketPriceCalculator

if __name__ == "__main__":
    calculator = TicketPriceCalculator()

    calculator.set_strategy(PriceStrategy.ADULT)
    print("Adult price:", calculator.calculateTicketPrice(10000))

    calculator.set_strategy(PriceStrategy.CHILD)
    print("Child price:", calculator.calculateTicketPrice(10000))

    calculator.set_strategy(PriceStrategy.STUDENT)
    print("Student price:", calculator.calculateTicketPrice(10000))