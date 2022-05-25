if __package__ is None or __package__ == '':
   # print('no package - init classes')
   from meals import *
   from abstract_meal import *
   from interfaces import *
   from meal_box import *
   from main_dish_builder import *
   from vegan_dish_builder import *
else:
   # print(f'package : {__package__} - init Classes')
   from .meals import *
   from .abstract_meal import *
   from .interfaces import *
   from .meal_box import *
   from .main_dish_builder import *
   from .vegan_dish_builder import *

if __name__ == "__main__":
   print('init arroz')