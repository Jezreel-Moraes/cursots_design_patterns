if __package__ is None or __package__ == '':
   # print('no package - Rice')
   from abstract_meal import AbstractMeal
else:
   # print(f'package : {__package__} - Rice')
   from .abstract_meal import AbstractMeal

class Rice(AbstractMeal): pass
class Beans(AbstractMeal): pass
class Meat(AbstractMeal): pass
class Beverage(AbstractMeal): pass
class Dessert(AbstractMeal): pass

if __name__ == "__main__":
   r = Rice("Arroz", 19)
   print(r.get_price())