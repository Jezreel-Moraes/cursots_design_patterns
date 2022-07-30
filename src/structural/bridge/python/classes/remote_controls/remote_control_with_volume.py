from classes.remote_controls.remote_control import RemoteControl


class RemoteControlWithVolume(RemoteControl):
    def volume_up(self) -> None:
        self.device.set_volume(self.device.get_volume() + 10)

    def volume_down(self) -> None:
        self.device.set_volume(self.device.get_volume() - 10)
