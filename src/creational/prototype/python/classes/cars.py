from enum import Enum

from classes.interfaces.car_protocol import Car


class CarTyping(Enum):
    SMALL_CAR = 'SmallCar'
    BIG_CAR = 'BigCar'


class SmallCar(Car):
    def __init__(self):
        super().__init__()
        self.type = CarTyping.SMALL_CAR

    def display_name(self):
        print("Inside SmallCar:display_name() method")


class BigCar(Car):
    def __init__(self):
        super().__init__()
        self.type = CarTyping.BIG_CAR

    def display_name(self):
        print("Inside BigCar:display_name() method.")
