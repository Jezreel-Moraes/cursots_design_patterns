from abc import ABCMeta


class UserProtocol(metaclass=ABCMeta):
    def __init__(self, name: str, location: str) -> None:
        self.name = name
        self.location = location

    def get_name(self): return self.name

    def get_location(self): return self.location

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} {self.__dict__}'
