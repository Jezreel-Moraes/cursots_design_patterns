from classes.interfaces.strategy_discount import StrategyDiscount


class DefaultDiscount(StrategyDiscount):
    def get_discount(self, shopping_cart) -> float:
        total = shopping_cart.get_total()

        if total >= 100 and total < 200:
            self.discount = 0.1
        elif total >= 200 and total < 300:
            self.discount = 0.2
        elif total >= 300:
            self.discount = 0.3

        return total * (1 - self.discount)
