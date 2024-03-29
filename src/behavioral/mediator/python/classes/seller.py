class SellerProduct:
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"{{ id: {self.id}, name: {self.name}, price: {self.price} }}"


class Seller:
    def __init__(self, name: str):
        self.name = name
        self.products: list[SellerProduct] = []
        self.mediator = None

    def show_products(self):
        for product in self.products:
            print(f'[{product.id}]: {product.name} - R$:{product.price:.2f}')

    def add_product(self, *products: SellerProduct):
        for product in products:
            self.products.append(product)

    def set_mediator(self, mediator) -> None:
        self.mediator = mediator

    def sell(self, id: str) -> SellerProduct | None:
        for index, product in enumerate(self.products):
            if product.id == id:
                return self.products.pop(index)
        return None

    def view_products(self):
        if not self.mediator:
            return
        self.mediator.show_products()

    def buy(self, id: str):
        if not self.mediator:
            return
        print(f'[Buyer] - {self.name}: {self.mediator.buy(id)}')
