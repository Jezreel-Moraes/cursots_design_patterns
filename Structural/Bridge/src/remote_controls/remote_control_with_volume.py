from .remote_control import RemoteControl

class RemoteControlWithVolume(RemoteControl):
   def volume_up(self) -> bool: 
      self.device.set_volume(self.device.get_volume() + 10)
   
   def volume_down(self) -> None: 
      self.device.set_volume(self.device.get_volume() - 10)
  