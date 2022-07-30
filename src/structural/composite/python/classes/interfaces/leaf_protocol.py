from abc import abstractmethod

from classes.interfaces.component_protocol import Component


class LeafComponent(Component):
    def __init__(self, name: str, price: int) -> None:
        super().__init__(name)
        self.price = price

    def add(self, *args) -> None:
        pass

    @abstractmethod
    def get_price(self) -> int: pass

    def __repr__(self) -> str:
        return f'{{{self.name}: {self.price}}}'
