from abc import ABCMeta, abstractclassmethod

class DevicesInterface(metaclass=ABCMeta):
   @abstractclassmethod
   def set_power(self, power_status: bool) -> None: pass
   
   @abstractclassmethod
   def get_power(self) -> bool: pass
   
   @abstractclassmethod
   def set_volume(self, volume: int) -> None: pass
  
   @abstractclassmethod
   def get_volume(self) -> int: pass
   
   @abstractclassmethod
   def get_name(self) -> str: pass