from classes.interfaces.smart_command_protocol import LightCommand
from classes.smart_house_light import SmartHouseLight


class LightPowerCommand(LightCommand):
    def __init__(self, light: SmartHouseLight) -> None:
        self.__light = light

    def execute(self) -> None:
        self.__light.on()

    def undo(self) -> None:
        self.__light.off()
