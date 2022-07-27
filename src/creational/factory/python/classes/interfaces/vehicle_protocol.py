import abc


class Vehicle(metaclass=abc.ABCMeta):
    def __init__(self, name: str) -> None:
        self.name = name

    def pick_up(self, customer_name: str) -> None:
        print(f'{self.name} is looking for {customer_name}')

    def stop(self) -> None:
        print(f'{self.name} stopped')

    def __repr__(self) -> str:
        return str(self.__dict__)
