from sys import path
path.insert(0, './src')

from vehicles import Bicycle, Vehicle

if __package__: from .vehicle_factory import VehicleFactory
else: from vehicle_factory import VehicleFactory

class BicycleFactory(VehicleFactory):
   def get_vehicle(self, vehicle_name: str) -> Vehicle: 
      return Bicycle(vehicle_name)
