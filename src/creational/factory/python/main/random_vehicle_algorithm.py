from sys import path
path.insert(0, './src')

from vehicles import Vehicle
from factories import *
from random import randint

def random(values: list):
   return values[randint(0,len(values) -1)]

def randomCarAlgorithm() -> Vehicle:
   car_factory = CarFactory()
   bicycle_factory = CarFactory()
   car1 = car_factory.get_vehicle('Celta')
   car2 = car_factory.get_vehicle('Corsa')
   bicycle = bicycle_factory.get_vehicle('Bicycle')
   vehicles = [car1, car2, bicycle]
   return random(vehicles)
   