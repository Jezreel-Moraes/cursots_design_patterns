from remote_controls import RemoteControl, RemoteControlWithVolume, remote_control
from devices import TV, Radio, radio

def main(remote_control: RemoteControl | RemoteControlWithVolume):
   print(remote_control.device.get_name())
   
   print(remote_control.device.get_power())
   remote_control.toggle_power()
   print(remote_control.device.get_power())
   
   if not isinstance(remote_control, RemoteControlWithVolume): return

   print(remote_control.device.get_volume())
   remote_control.volume_up()
   print(remote_control.device.get_volume())
   remote_control.volume_down()
   print(remote_control.device.get_volume())


if __name__ == '__main__':
   
   tv = TV()
   radio = Radio()
   
   remote_control = RemoteControl(tv)
   remote_control_with_volume = RemoteControlWithVolume(radio)
   
   main(remote_control)
   print()
   main(remote_control_with_volume)