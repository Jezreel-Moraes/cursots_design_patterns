from faker import Faker

faker = Faker()

class AbstractMealSpy():
   def __init__(self) -> None:
      self.name = faker.name()
      self.price = faker.random_int()
   
   def get_price(self): 
      return self.price

class AbstractMealWithOutNameSpy():
   def __init__(self) -> None:
      self.price = faker.random_int()
   
   def get_price(self): return int()
   
class AbstractMealWithOutPriceSpy():
   def __init__(self) -> None:
      self.name = faker.name()
   
   def get_price(self): return int()
   
class AbstractMealWithOutGetPriceSpy():
   def __init__(self) -> None:
      self.name = faker.name()
      self.price = faker.random_int()

if __name__ == '__main__':
   pass