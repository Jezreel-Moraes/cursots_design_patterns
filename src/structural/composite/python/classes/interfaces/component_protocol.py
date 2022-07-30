from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    @abstractmethod
    def add(self, *args) -> None: pass

    @abstractmethod
    def get_price(self) -> int: pass
