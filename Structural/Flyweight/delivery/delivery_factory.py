from typing import Dict
from .delivery_location_data import DeliveryLocationData
from .delivery_flyweight import DeliveryFlyweight
from .delivery_location import DeliveryLocation


class DeliveryFactory:
   def __init__(self) -> None:
      self.locations: Dict[str, DeliveryLocation] = {}
   
   @staticmethod
   def __create_id(data: DeliveryLocationData) -> str:
      return '_'.join(map(lambda value: value.replace(' ','').lower(),[data.city, data.street]))
   
   def create_location(self, intrinsicState: DeliveryLocationData) -> DeliveryFlyweight:
      key = self.__create_id(intrinsicState)
      if (not key in self.locations.keys()):
         self.locations[key] = DeliveryLocation(intrinsicState)
      return self.locations[key]
   
   def get_locations(self):
      return dict(self.locations)