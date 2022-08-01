from classes.interfaces.strategy_discount import StrategyDiscount


class NewDiscount(StrategyDiscount):
    def get_discount(self, shopping_cart):
        total = shopping_cart.get_total()

        if total >= 150:
            self.discount = 0.05

        return total * (1 - self.discount)
