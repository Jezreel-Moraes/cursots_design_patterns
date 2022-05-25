from sys import path
path.insert(0, './src')

from classes import Customer1, Vehicle1
from interfaces import *

class CustomerVehicleFactory1(ICustomerVehicleFactory):
   @staticmethod
   def create_customer(name: str, location: str) -> ICostumer:
      return Customer1(name, location)
      
   @staticmethod
   def create_vehicle(name: str) -> IVehicle:
      return Vehicle1(name)
      