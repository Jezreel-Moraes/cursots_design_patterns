from operator import xor
from re import L
from typing import List
from functools import reduce 

if __package__ is None or __package__ == '':
   # print('no package - init Meal Box')
   from interfaces import MealCompositeProtocol
   from abstract_meal import AbstractMeal
else:
   # print(f'package : {__package__} - Meal Box')
   from .interfaces import MealCompositeProtocol
   from .abstract_meal import AbstractMeal

class MealBox(MealCompositeProtocol):
   def __init__(self) -> None:
      self._children : List[AbstractMeal] = list()
   
   def get_price(self) -> int:
      return reduce(lambda sum, meal: sum + meal.get_price() , self._children, 0) 

   @staticmethod
   def _meal_validate(meal : AbstractMeal) -> bool:
      
      try:
         name = getattr(meal, 'name')
      except Exception:
         raise Exception("The meal must have 'name' atribute!")
      
      try:
         price = getattr(meal, 'price')
      except Exception:
         raise Exception("The meal must have 'price' atribute!")
      
      try:
         get_price = getattr(meal, 'get_price')
      
         if not callable(get_price): 
            raise Exception()
         
      except Exception:
         raise Exception("The meal must have 'get_price' method!")
         

      return True 

   def add(self, meals : List[AbstractMeal] | AbstractMeal) -> None:
      
      if not isinstance(meals, list):
         if MealBox._meal_validate(meal=meals):
            self._children.append(meals)
            return
            
      for meal in meals: 
         if MealBox._meal_validate(meal=meal):
            self._children.append(meal)

   def __repr__(self) -> str:
      children = str({'_children' : self._children})
      return str(f" { self.__class__.__name__ } { children }")
   
if __name__ == "__main__": 
   pass