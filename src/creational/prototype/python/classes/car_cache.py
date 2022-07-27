from enum import Enum
from typing import Callable, Dict

from classes.cars import BigCar, SmallCar
from classes.interfaces.car_protocol import Car


class Ids(Enum):
    BIG_CAR = '1'
    SMALL_CAR = '2'


class CarsCache:
    __CARS: Dict[Ids, Car] = {}

    @staticmethod
    def __load(id: Ids) -> None:
        CAR_DICT: Dict[Ids, Callable] = {
            Ids.BIG_CAR: CarsCache.__load_big_car,
            Ids.SMALL_CAR: CarsCache.__load_small_car,
        }

        CAR_DICT[id]()

    @staticmethod
    def get_car(id: Ids) -> Car:
        if id not in CarsCache.__CARS.keys():
            CarsCache.__load(id)

        CAR = CarsCache.__CARS.get(id, None)
        return CAR.clone()

    @staticmethod
    def __load_big_car() -> None:
        print('\nloading BigCar')

        BIG_CAR = BigCar()
        BIG_CAR.set_id(Ids.BIG_CAR)
        CarsCache.__CARS[BIG_CAR.get_id()] = BIG_CAR

        print('finished loading\n')

    @staticmethod
    def __load_small_car() -> None:
        print('loading SmallCar')

        SMALL_CAR = SmallCar()
        SMALL_CAR.set_id(Ids.SMALL_CAR)
        CarsCache.__CARS[SMALL_CAR.get_id()] = SMALL_CAR

        print('finished loading\n')
