from .devices_interface import DevicesInterface

class TV(DevicesInterface):
   def __init__(self) -> None:
      self.name: str = 'TV'
      self.volume: int = 10
      self.power: bool = False
   
   def set_power(self, power_status: bool) -> None:
      self.power = power_status

   def get_power(self) -> bool:
      return self.power

   def set_volume(self, volume: int) -> None:
      if volume > 100 or volume < 0: return
      self.volume = volume

   def get_volume(self) -> int:
      return self.volume

   def get_name(self) -> str:
      return self.name
   
   