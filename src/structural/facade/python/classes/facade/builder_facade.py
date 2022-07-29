import sys

sys.path.insert(0, './src/creational/builder/python')


if True:
    from classes.builder.main_dish_builder import MainDishBuilder
    from classes.builder.vegan_dish_builder import VeganDishBuilder
    from classes.meal_box import MealBox
    from classes.meals import Beans, Meat, Rice


class BuilderFacade():

    def __init__(self):
        self.main_dish_builder = MainDishBuilder()
        self.vegan_dish_builder = VeganDishBuilder()

        self.RICE = Rice('Arroz', 5)
        self.BEANS = Beans('Feijão', 10)
        self.MEAT = Meat('Carne', 20)

    def make_meal_with_two_builder(self):
        meal1 = self.main_dish_builder.make_meal().make_dessert().get_meal()
        print(meal1)
        print(meal1.get_price())

        meal2 = self.vegan_dish_builder.make_meal().get_meal()
        print(meal2)
        print(meal2.get_price())

    def make_meal_without_builder(self):

        meal_box = MealBox()
        meal_box.add(self.RICE, self.BEANS, self.MEAT)

        print(meal_box._children)
        print(meal_box.get_price())
