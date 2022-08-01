from classes.interfaces.product_protocol import ProductProtocol
from classes.interfaces.strategy_discount import StrategyDiscount


class ShoppingCart:
    def __init__(self) -> None:
        self.products: list[ProductProtocol] = []
        self.discountStrategy = StrategyDiscount()

    def set_discount_strategy(self, strategy: StrategyDiscount) -> None:
        self.discountStrategy = strategy

    def add_products(self, *products: ProductProtocol) -> None:
        for product in products:
            self.products.append(product)

    def get_products(self) -> list[ProductProtocol]:
        return self.products

    def get_total(self) -> float:
        return sum(product.price for product in self.products)

    def get_total_with_discount(self) -> float:
        return self.discountStrategy.get_discount(self)
