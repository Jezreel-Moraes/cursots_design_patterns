from classes.interfaces.meal_builder_protocol import MealBuilderProtocol
from classes.meal_box import MealBox
from classes.meals import Beans, Beverage, Dessert, Rice


class VeganDishBuilder(MealBuilderProtocol):
    def __init__(self) -> None:
        self._meal: MealBox = MealBox()

    def reset(self) -> type:
        self._meal = MealBox()
        return self

    def make_beverage(self) -> type:
        BEVERAGE = Beverage('Bebida', 7)
        self._meal.add(BEVERAGE)
        return self

    def make_dessert(self) -> type:
        DESSERT = Dessert('Sobremesa', 10)
        self._meal.add(DESSERT)
        return self

    def make_meal(self) -> type:
        RICE = Rice('Arroz', 5)
        BEANS = Beans('Feijão', 10)
        self._meal.add(RICE, BEANS)
        return self

    def get_meal(self) -> MealBox:
        return self._meal

    def get_price(self) -> int:
        return self._meal.get_price()
