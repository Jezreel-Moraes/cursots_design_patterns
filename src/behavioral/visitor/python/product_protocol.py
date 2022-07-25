from abc import ABC, abstractmethod


class VisitableProductProtocol(ABC):
    
   def __init__(self, name: str, price: int) -> None:
      self.name = name
      self.price = price
   
   def get_name(self): 
      return self.name 
   
   def get_price(self): 
      return self.price 
   
   @abstractmethod
   def get_price_with_taxes(self):
      pass