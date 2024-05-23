from Ejercicio1.PriceStrategy import PriceStrategy


class StudentStrategy(PriceStrategy):
 def calculate_price(self, base_price: int) -> float: return base_price * 0.8