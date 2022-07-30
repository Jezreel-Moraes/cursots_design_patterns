from classes.interfaces.devices_interface import DevicesInterface


class RemoteControl():
    def __init__(self, device: DevicesInterface) -> None:
        self.device = device

    def toggle_power(self) -> None:
        self.device.set_power(not self.device.get_power())
