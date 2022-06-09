from .product_protocol import ProductProtocol

class PrintedTShirtDecorator(ProductProtocol):
   
    def __init__(self, product: ProductProtocol) -> None:
        self.product = product
        
    def get_price(self) -> int:
        return self.product.get_price() + 10
        

    def get_name(self) -> str:
        return self.product.get_name() + ' (printed)'