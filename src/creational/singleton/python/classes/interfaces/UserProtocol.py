from abc import ABCMeta


class User(metaclass=ABCMeta):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return str(self.__dict__)
