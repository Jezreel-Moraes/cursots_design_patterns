class DeliveryLocationData:
   def __init__(self, city: str, street: str):
      self.__CITY = city
      self.__STREET = street
        
   @property
   def city(self) -> str: return self.__CITY
        
   @property
   def street(self) -> str: return self.__STREET
   
   def __repr__(self) -> str:
      return str(f'city: {self.__CITY}, street: {self.__STREET}')
   
