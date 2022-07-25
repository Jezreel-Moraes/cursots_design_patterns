from abc import ABCMeta, abstractclassmethod
from .ICustomer import ICostumer
from .IVehicle import IVehicle

class ICustomerVehicleFactory(metaclass=ABCMeta):
   @abstractclassmethod
   def create_customer(name: str, location: str) -> ICostumer: pass
   
   @abstractclassmethod
   def create_vehicle(name: str) -> IVehicle: pass
      
      