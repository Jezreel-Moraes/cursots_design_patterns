from sys import path
path.insert(0, './src')

from interfaces import IVehicle

class Vehicle2(IVehicle):
   def get_name(self): return self.name
   
   def pick_up(self, customer_name: str): 
      self.customer = customer_name
      print(f'{self.get_name()} is looking for {customer_name}')

   def get_customer(self): return self.customer if self.customer else None

   def say_poggers(self): print('poggers: Vehicle 2 muito pica')
      