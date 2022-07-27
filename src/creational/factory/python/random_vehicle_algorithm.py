from random import randint

from classes.factories.car_factory import CarFactory
from classes.interfaces.vehicle_protocol import Vehicle

CAR_FACTORY = CarFactory()
BICYCLE_FACTORY = CarFactory()

VEHICLES = [
    CAR_FACTORY.get_vehicle('Celta'),
    CAR_FACTORY.get_vehicle('Corsa'),
    BICYCLE_FACTORY.get_vehicle('Bicycle'),
]


def randomCarAlgorithm() -> Vehicle:
    return VEHICLES[randint(0, len(VEHICLES) - 1)]
