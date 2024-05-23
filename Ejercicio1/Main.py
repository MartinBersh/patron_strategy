from Ejercicio1.AdultStrategy import AdultStrategy
from Ejercicio1.ChildStrategy import ChildStrategy
from Ejercicio1.StudentStrategy import StudentStrategy
from Ejercicio1.TicketPriceCalculator import TicketPriceCalculator

if __name__ == "__main__":
 calculator = TicketPriceCalculator(AdultStrategy())
 print("Adult price:", calculator.calculate(100))
 calculator.set_strategy(ChildStrategy())
 print("Child price:", calculator.calculate(100))
 calculator.set_strategy(StudentStrategy())
 print("Student price:", calculator.calculate(100))