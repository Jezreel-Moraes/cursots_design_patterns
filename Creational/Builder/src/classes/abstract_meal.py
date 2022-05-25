if __package__ is None or __package__ == '':
   # print('no package - Abstract Meal')
   from interfaces import MealCompositeProtocol
else:
   # print(f'package : {__package__} - Abstract Meal')
   from .interfaces import MealCompositeProtocol
   
class AbstractMeal(MealCompositeProtocol):
   def __init__(self, name : str, price : int) -> None:
      
      if not isinstance(name, str): 
         raise TypeError("'name' must be string!")
      
      if not isinstance(price, int): 
         raise TypeError("'price' must be integer!")
      
      self.name : str = name
      self.price : int = price
   
   def get_price(self) -> int:
      return int(self.price)
   
   def __repr__(self) -> str:
      return str(f'{self.__class__.__name__} {self.__dict__}')


if __name__ == '__main__':
   abs = AbstractMeal(12, 'huiASDUI')
   print(abs.get_price())