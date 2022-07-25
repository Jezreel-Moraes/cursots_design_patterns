from mediator import Mediator


class Buyer:
   def __init__(self, name: str, mediator: Mediator):
      self.name = name
      self.mediator = mediator
      
   def view_products(self):
       self.mediator.show_products()
       
   def buy(self, id: str):
      print(f'[Buyer] - {self.name}: {self.mediator.buy(id)}')
       