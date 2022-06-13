from .smart_command_protocol import LightCommand
from .smart_house_light import SmartHouseLight

class LightIntensityCommand(LightCommand):
   def __init__(self, light: SmartHouseLight) -> None:
      self.__light = light
      
   def execute(self) -> None:
      self.__light.increase_intensity()
      
   def undo(self) -> None:
      self.__light.decrease_intensity()