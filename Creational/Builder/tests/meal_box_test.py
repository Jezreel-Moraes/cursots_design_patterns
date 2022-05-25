import sys, unittest
from functools import reduce 
from faker import Faker
sys.path.insert(0, './src')
from classes import MealBox
from resources import *

faker = Faker()

class MealBoxTest(unittest.TestCase):
   
   def test_mealBox_passing_argument(self):
      argument = faker.name()
      
      with self.assertRaises(TypeError):
         meal_box = MealBox(argument)
   
   def test_mealBox_instancing(self):
      meal_box = MealBox()
      self.assertTrue(isinstance(meal_box, MealBox))
   
   def test_mealValidate_with_random_value(self):
      argument_1 = faker.name()
      argument_2 = faker.random_int()
      
      with self.assertRaises(Exception):
         MealBox._meal_validate(argument_1)
      
      with self.assertRaises(Exception):
         MealBox._meal_validate(argument_2)
      
      with self.assertRaises(Exception):
         MealBox._meal_validate(None)
      
      
   def test_mealValidate_with_spy_without_name(self):
      spy = AbstractMealWithOutNameSpy()
      
      with self.assertRaises(Exception):
         MealBox._meal_validate(spy)
      
   def test_mealValidate_with_spy_without_price(self):
      spy = AbstractMealWithOutPriceSpy()
      
      with self.assertRaises(Exception):
         MealBox._meal_validate(spy)
      
   def test_mealValidate_with_spy_without_get_price(self):
      spy = AbstractMealWithOutGetPriceSpy()
      
      with self.assertRaises(Exception):
         MealBox._meal_validate(spy)
         
   def test_add_with_empty_list(self):
      meal_box = MealBox()
      meal_box.add(list())
      
      self.assertFalse(bool(meal_box._children))
         
   def test_add_with_single_spy(self):
      spy = AbstractMealSpy()
      meal_box = MealBox()
      meal_box.add(spy)
      
      SPY_INDEX = 0
      
      self.assertTrue(bool(meal_box._children)) # is not empty
      self.assertEqual(meal_box._children[SPY_INDEX], spy)
         
   def test_add_with_multiple_spies(self):
      spies_number = faker.random_int(min=2,max=30)
      spies = [AbstractMealSpy() for i in range(spies_number)]
      meal_box = MealBox()
      meal_box.add(spies)
      
      self.assertTrue(bool(meal_box._children)) # is not empty
      self.assertEqual(len(meal_box._children), len(spies))
      
      for value, spy in zip(meal_box._children, spies):
         self.assertEqual(value, spy)
   
   def test_get_price_with_no_values_add(self):
      meal_box = MealBox()
      EMPTY_PRICE = 0
      
      self.assertEqual(meal_box.get_price(), EMPTY_PRICE)
      
   def test_get_price_with_single_spy(self):
      spy = AbstractMealSpy()
      meal_box = MealBox()
      meal_box.add(spy)
      
      self.assertEqual(meal_box.get_price(), int(spy.price))
   
   def test_get_price_with_multiple_spies(self):
      spies_number = faker.random_int(min=2,max=30)
      spies = [AbstractMealSpy() for _ in range(spies_number)]
      total_price = reduce(lambda sum, spy: sum + spy.get_price(), spies, 0)
      meal_box = MealBox()
      meal_box.add(spies)
      
      self.assertEqual(meal_box.get_price(), total_price)

if __name__ == '__main__':
   unittest.main()   
   