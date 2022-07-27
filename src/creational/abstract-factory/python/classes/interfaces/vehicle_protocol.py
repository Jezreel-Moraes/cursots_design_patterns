from abc import ABCMeta, abstractclassmethod


class VehicleProtocol(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str: return self.name

    @abstractclassmethod
    def pick_up(self, user_name: str) -> None: pass

    @abstractclassmethod
    def get_user(self) -> str: pass

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} {self.__dict__}'
