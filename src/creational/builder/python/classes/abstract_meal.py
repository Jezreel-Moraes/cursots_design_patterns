from classes.interfaces.meal_composite_protocol import MealCompositeProtocol


class AbstractMeal(MealCompositeProtocol):
    def __init__(self, name: str, price: int) -> None:

        self.name = name
        self.price = price

    def get_price(self) -> int:
        return self.price

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} {self.__dict__}'
