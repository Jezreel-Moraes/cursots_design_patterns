class StrategyDiscount:
   def __init__(self):
      self.discount = float()

   def get_discount(self, shopping_cart):
      return shopping_cart.get_total()