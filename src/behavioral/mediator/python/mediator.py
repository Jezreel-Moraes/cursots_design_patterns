from seller import Seller, SellerProduct


class Mediator:
    def __init__(self):
        self.sellers = []
        
    def add_seller(self, sellers: list | Seller):
        if isinstance(sellers, list):
            for seller in sellers:
                self.sellers.append(seller)
                seller.set_mediator(self) 
        
        else: self.sellers.append(sellers)
            
    def buy(self, id: str) -> SellerProduct | None:
        for seller in self.sellers:
            product = seller.sell(id)
            if product: 
                return f'Here is product[{product.id}]:\n > {product.name} - R$:{product.price:.2f}\n > [Seller]: {seller.name}\n'
                
        return f'\n > Product with id {id} not found'
        
    def show_products(self):
        print('\nAll products:\n')
        for seller in self.sellers:
            print(f'Seller - {seller.name}: ')
            seller.show_products()
            print('\n')