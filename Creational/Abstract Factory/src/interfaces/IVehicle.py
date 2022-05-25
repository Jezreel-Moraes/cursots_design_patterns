from abc import ABCMeta, abstractclassmethod

class IVehicle(metaclass=ABCMeta):
   def __init__(self, name: str) -> None:
      self.name = name
   
   @abstractclassmethod
   def get_name(self): pass
   
   @abstractclassmethod
   def pick_up(self, customer_name: str): pass

   @abstractclassmethod
   def get_customer(self): pass