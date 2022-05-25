from abc import ABCMeta, abstractclassmethod

class ICostumer(metaclass=ABCMeta):
   def __init__(self, name: str, location: str) -> None:
      self.name = name
      self.location = location
      
   @abstractclassmethod
   def get_name(self): pass
   
   @abstractclassmethod
   def get_location(self): pass