from functools import reduce
from typing import List

from classes.abstract_meal import AbstractMeal
from classes.interfaces.meal_composite_protocol import MealCompositeProtocol


class MealBox(MealCompositeProtocol):
    def __init__(self) -> None:
        self._children: List[AbstractMeal] = []

    def get_price(self) -> int:
        return reduce(
            lambda sum, meal: sum + meal.get_price(), self._children, 0)

    def add(self, *meals: AbstractMeal) -> None:
        for meal in meals:
            self._children.append(meal)

    def __repr__(self) -> str:
        children = {'_children': self._children}
        return f"{ self.__class__.__name__ }{ children }"
