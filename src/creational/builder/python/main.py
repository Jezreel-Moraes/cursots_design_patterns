from classes.builder.main_dish_builder import MainDishBuilder
from classes.builder.vegan_dish_builder import VeganDishBuilder


def main():
    main_dish_builder = MainDishBuilder()
    meal1 = main_dish_builder.make_meal().make_dessert().get_meal()
    print(meal1)
    print(meal1.get_price())

    vegan_dish_builder = VeganDishBuilder()
    meal2 = vegan_dish_builder.make_meal().get_meal()
    print(meal2)
    print(meal2.get_price())


if __name__ == "__main__":
    main()
