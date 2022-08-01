class StrategyDiscount:
    def __init__(self):
        self.discount = float()

    def get_discount(self, shopping_cart) -> float:
        return shopping_cart.get_total()
