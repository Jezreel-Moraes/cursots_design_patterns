from sys import path
path.insert(0, './src')

from interfaces import ICostumer

class Customer2(ICostumer):
   def get_name(self): return self.name
   def get_location(self): return self.location
   def say_poggers(self): print('Custumer 2 muito pica')