from sys import path
path.insert(0, './src')

from classes import Customer2, Vehicle2
from interfaces import *

class CustomerVehicleFactory2(ICustomerVehicleFactory):
   @staticmethod
   def create_customer(name: str, location: str) -> ICostumer:
      return Customer2(name, location)
   
   @staticmethod
   def create_vehicle(name: str) -> IVehicle:
      return Vehicle2(name)
      