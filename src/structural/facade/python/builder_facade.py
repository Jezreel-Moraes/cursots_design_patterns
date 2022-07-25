import sys
sys.path.insert(0, './Creational/Builder/src')

from classes.meals import *
from classes import MealBox, MainDishBuilder, VeganDishBuilder

class BuilderFacade():

   def __init__(self):
      self.main_dish_builder = MainDishBuilder()
      self.vegan_dish_builder = VeganDishBuilder()
      
      self.RICE = Rice('Arroz', 5)
      self.BEANS = Beans('Feijao', 10)
      self.MEAT = Meat('Carne', 20)

   def make_meal_with_two_builder(self):
      meal1 = self.main_dish_builder.make_meal().make_dessert().get_meal()
      print(meal1)
      print(meal1.get_price())
      
      meal2 = self.vegan_dish_builder.make_meal().get_meal()
      print(meal2)
      print(meal2.get_price())
      
   def make_meal_with_builder_2(self):
      meal1 = self.main_dish_builder.make_meal().make_dessert().get_meal()
      
      print(meal1)
      print(meal1.get_price())
      
      self.main_dish_builder.reset()
      meal2 = self.main_dish_builder.make_meal().get_meal()
      
      print(meal2)
      print(meal2.get_price())
      
      print('\n', meal1)
      print(meal1.get_price())
      
      print(meal1 == meal2)

   def make_meal_with_builder_1(self):
      # com builder
      self.main_dish_builder.make_meal().make_dessert()
      print(self.main_dish_builder.get_meal())
      print(self.main_dish_builder.get_price())
   
   def make_meal_without_builder(self):
      
      meal_box = MealBox()
      meal_box.add([self.RICE, self.BEANS, self.MEAT])
      
      print(meal_box._children)
      print(meal_box.get_price())

   def make_meal_build_without_list(self):
      print(self.main_dish_builder.make_rice().get_meal())
      print(self.main_dish_builder.get_price())


class BuilderFacadeDecorator():
   def __init__(self):
      self.facade = BuilderFacade()
      
   def before(self):
      self.facade.main_dish_builder.reset()
      self.facade.vegan_dish_builder.reset()
      
   def make_meal_with_two_builder(self):
      self.before()
      self.facade.make_meal_with_two_builder()
      print('\n >> Finish make_meal_with_two_builder\n')

   def make_meal_with_builder_2(self):
      self.before()
      self.facade.make_meal_with_builder_2()
      print('\n >> Finish make_meal_with_builder_2\n')

   def make_meal_with_builder_1(self):
      self.before()
      self.facade.make_meal_with_builder_1()
      print('\n >> Finish make_meal_with_builder_1\n')

   def make_meal_without_builder(self):
      self.before()
      self.facade.make_meal_without_builder()
      print('\n >> Finish make_meal_without_builder\n')

   def make_meal_build_without_list(self):
      self.before()
      self.facade.make_meal_build_without_list()
      print('\n >> Finish make_meal_build_without_list\n')
      
