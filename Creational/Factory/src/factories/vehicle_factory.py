from abc import ABCMeta, abstractclassmethod
from sys import path
path.insert(0, './src')
from vehicles import Vehicle


class VehicleFactory(metaclass=ABCMeta):
   @abstractclassmethod
   def get_vehicle(self, vehicle_name: str) -> Vehicle: pass
   
   def pick_up(self, customer_name: str, vehicle_name: str) -> Vehicle:
      car = self.get_vehicle(vehicle_name)
      car.pick_up(customer_name)
      return car

   