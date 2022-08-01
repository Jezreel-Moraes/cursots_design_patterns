class SmartHouseLight:
    def __init__(self, name):
        self.__name = name
        self.__isOn = False
        self.__intensity = 0

    def get_power_status(self):
        status = 'ON' if self.__isOn else 'OFF'
        return f'The light {self.__name} is {status}'

    def on(self):
        self.__isOn = True
        print(self.get_power_status())

    def off(self):
        self.__isOn = False
        print(self.get_power_status())

    def get_intensity_status(self):
        return f'The light intensity of {self.__name} is {self.__intensity}%'

    def increase_intensity(self):
        self.__intensity = min(self.__intensity + 1, 100)
        print(self.get_intensity_status())

    def decrease_intensity(self):
        self.__intensity = max(self.__intensity - 1, 0)
        print(self.get_intensity_status())
