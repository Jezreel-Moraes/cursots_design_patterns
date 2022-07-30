from classes.interfaces.component_protocol import Component


class Compositor(Component):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.children: list[Component] = []

    def add(self, *args: Component) -> None:
        for item in args:
            self.children.append(item)

    def get_price(self) -> int:
        sum = 0
        for component in self.children:
            sum += component.get_price()
        return sum
