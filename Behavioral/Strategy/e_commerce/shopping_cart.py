from functools import reduce
from typing import List
from .product_protocol import ProductProtocol
from .strategies import StrategyDiscount

class ShoppingCart:
   def __init__(self) -> None:
      self.products: List[ProductProtocol] = []
      self.discountStrategy = StrategyDiscount()
   
   def set_discount_strategy(self, strategy: StrategyDiscount) -> None:
      self.discountStrategy = strategy
      
   def add_products(self, products: List[ProductProtocol]) -> None:
      if type(products) is ProductProtocol: self.products.append(products)
      if type(products) is not list: return
      for product in products: self.products.append(product)   
   
   def get_products(self) -> List[ProductProtocol]:
      return self.products
   
   def get_total(self) -> float:
     return float(reduce(lambda sum, product: sum + product.price, self.products, 0))
  
   def get_total_with_discount(self) -> float:
      return self.discountStrategy.get_discount(self)