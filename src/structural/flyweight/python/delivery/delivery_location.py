from .delivery_flyweight import DeliveryFlyweight
from .delivery_location_data import DeliveryLocationData

class DeliveryLocation(DeliveryFlyweight):
   def __init__(self, intrinsic_state: DeliveryLocationData) -> None:
      self.__INTRINSIC_STATE = intrinsic_state
   
   @property
   def intrinsic_state(self) -> DeliveryLocationData:
      return self.__INTRINSIC_STATE
   
   def deliver(self, name: str, number: str) -> None:
      print(f'Deliver to {name}')
      print(f'On street {self.intrinsic_state.street}, city {self.intrinsic_state.city}')
      print(f'Number: {number}')
      print('----------------------------')
      
   def __repr__(self) -> str:
      return str(f'{self.__class__.__name__} {{ {self.intrinsic_state} }}')
   