if __package__ is None or __package__ == '':
   # print('no package - init Main')
   from classes.meals import *
   from classes import MealBox, MainDishBuilder, VeganDishBuilder
else:
   # print(f'package : {__package__} - Main')
   from .classes.meals import *
   from .classes import MealBox, MainDishBuilder, VeganDishBuilder

# functional tests

def with_two_builder():
   main_dish_builder = MainDishBuilder()
   meal1 = main_dish_builder.make_meal().make_dessert().get_meal()
   print(meal1)
   print(meal1.get_price())
   
   vengan_dish_builder = VeganDishBuilder()
   meal2 = vengan_dish_builder.make_meal().get_meal()
   print(meal2)
   print(meal2.get_price())
   
def with_builder_2():
   main_dish_builder = MainDishBuilder()
   meal1 = main_dish_builder.make_meal().make_dessert().get_meal()
   
   print(meal1)
   print(meal1.get_price())
   
   main_dish_builder.reset()
   meal2 = main_dish_builder.make_meal().get_meal()
   
   print(meal2)
   print(meal2.get_price())
   
   print('\n', meal1)
   print(meal1.get_price())
   
   print(meal1 == meal2)

def with_builder_1():
   # com builder
   main_dish_builder = MainDishBuilder()
   main_dish_builder.make_meal().make_dessert()
   print(main_dish_builder.get_meal())
   print(main_dish_builder.get_price())
   
def without_builder():
   # sem builder
   RICE = Rice('Arroz', 5)
   BEANS = Beans('Feijao', 10)
   MEAT = Meat('Carne', 20)
   
   meal_box = MealBox()
   meal_box.add([RICE, BEANS, MEAT])
   
   print(meal_box._children)
   print(meal_box.get_price())

def build_without_list():
   main_dish_builder = MainDishBuilder()
   print(main_dish_builder.make_rice().get_meal())
   print(main_dish_builder.get_price())

if __name__ == "__main__":
   build_without_list()