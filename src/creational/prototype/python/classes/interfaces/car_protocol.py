from abc import ABCMeta, abstractmethod
from copy import copy


class Car(metaclass=ABCMeta):

    def __init__(self):

        for i in range(10000):
            for n in range(1000):
                if i != 0 and n != 0 and i % n != 0:
                    _ = i*n

        print(' > Creating new car:', self.__class__.__name__)
        self.id = None
        self.type = None

    @abstractmethod
    def display_name(self) -> None:
        pass

    def set_type(self, type: str) -> None:
        self.type = type

    def get_type(self) -> str:
        return self.type

    def get_id(self) -> str:
        return self.id

    def set_id(self, id) -> None:
        self.id = id

    def clone(self) -> object:
        return copy(self)
