from classes.interfaces.product_protocol import ProductProtocol


class TShirt(ProductProtocol):
    def __init__(self):
        self.price = 49.9
        self.name = 'TShirt'

    def get_price(self) -> int:
        return self.price

    def get_name(self) -> str:
        return self.name
