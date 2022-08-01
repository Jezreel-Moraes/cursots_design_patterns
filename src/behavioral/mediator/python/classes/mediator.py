from classes.seller import Seller


class Mediator:
    def __init__(self) -> None:
        self.sellers: list[Seller] = []

    def add_seller(self, *sellers: Seller) -> None:
        for seller in sellers:
            self.sellers.append(seller)
            seller.set_mediator(self)

    def buy(self, id: str) -> str:
        for seller in self.sellers:
            product = seller.sell(id)
            if product:
                return f'Here is product[{product.id}]:\n > {product.name}' + \
                    f' - R$:{product.price:.2f}\n > [Seller]: {seller.name}\n'

        return f'\n > Product with id {id} not found'

    def show_products(self) -> None:
        print('\nAll products:\n')
        for seller in self.sellers:
            print(f'[Seller] - {seller.name}: ')
            seller.show_products()
            print()
