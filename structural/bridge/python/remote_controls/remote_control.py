from sys import path
path.insert(0, './src')

from devices import DevicesInterface

class RemoteControl():
   def __init__(self, device: DevicesInterface) -> None:
       self.device = device
   
   def toggle_power(self) -> None:
      self.device.set_power(not self.device.get_power())
      
   