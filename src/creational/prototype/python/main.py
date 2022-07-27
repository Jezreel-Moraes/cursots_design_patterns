from typing import List

from classes.car_cache import CarsCache, Ids
from classes.cars import BigCar
from classes.interfaces.car_protocol import Car


def main():
    LIST_ONE: List[Car] = []
    LIST_TWO: List[Car] = []

    print('without cache:\n')
    for _ in range(10):
        CAR = BigCar()
        CAR.set_id(Ids.BIG_CAR)
        LIST_ONE.append(CAR)

    print('\nwith cache:\n')
    for _ in range(10):
        LIST_TWO.append(CarsCache.get_car(Ids.BIG_CAR))

    print('LIST_ONE = [')
    for item in LIST_ONE:
        print(f'  {item}')
    print(']\n\n')

    print('LIST_TWO = [')
    for item in LIST_TWO:
        print(f'  {item}')
    print(']\n\n')


if __name__ == '__main__':
    main()
