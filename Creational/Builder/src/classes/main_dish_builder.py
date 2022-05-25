if __package__ is None or __package__ == '':
   # print(f'no package - init Interfaces')
   from interfaces import MealBuilderProtocol
   from meal_box import MealBox
   from meals import *
else:
   # print(f'package : {__package__} - init Interfaces')
   from .interfaces import MealBuilderProtocol
   from .meal_box import MealBox
   from .meals import *

class MainDishBuilder(MealBuilderProtocol):
   def __init__(self) -> None:
      self._meal : MealBox = MealBox()
   
   def reset(self) -> type:
      self._meal = MealBox()
      return self   
   
   def make_meal(self) -> type:
      RICE = Rice('Arroz', 5)
      BEANS = Beans('Feijao', 10)
      MEAT = Meat('Carne', 20)
      self._meal.add([RICE, BEANS, MEAT])
      return self

   def make_rice(self) -> type:
      RICE = Rice('Arroz', 6)
      self._meal.add(RICE)
      return self

   def make_beverage(self) -> type:
      BEVERAGE = Beverage('Bebida', 7)
      self._meal.add([BEVERAGE])
      return self
   
   def make_dessert(self) -> type: 
      DESSERT = Dessert('Sobremesa', 10)
      self._meal.add([DESSERT])
      return self
   
   def get_meal(self) -> MealBox:
      return self._meal
   
   def get_price(self) -> int:
      return self._meal.get_price()