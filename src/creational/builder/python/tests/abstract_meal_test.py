from classes.abstract_meal import AbstractMeal
import sys
import unittest

from faker import Faker

sys.path.insert(0, './src')

faker = Faker()


class AbstractMealTest(unittest.TestCase):

    def test_abstractMeal_with_no_arguments(self):
        with self.assertRaises(TypeError):
            abstract_meal = AbstractMeal()

    def test_abstractMeal_with_wrong_arguments(self):
        name = faker.random_int()
        price = faker.name()

        self.assertTrue(isinstance(name, int))
        self.assertTrue(isinstance(price, str))

        with self.assertRaises(TypeError):
            abstract_meal = AbstractMeal(name=name, price=price)

    def test_get_price_with_random_values(self) -> None:
        name = faker.name()
        price = faker.random_int()

        self.assertTrue(isinstance(name, str))
        self.assertTrue(isinstance(price, int))

        abstract_meal = AbstractMeal(name=name, price=price)

        self.assertEqual(abstract_meal.get_price(), price)

    def test_get_price_with_name_and_no_price(self):
        name = faker.name()

        self.assertTrue(isinstance(name, str))

        with self.assertRaises(TypeError):
            abstract_meal = AbstractMeal(name=name)

    def test_abstractMeal_parameters_pass(self):
        name = faker.name()
        price = faker.random_int()

        self.assertTrue(isinstance(name, str))
        self.assertTrue(isinstance(price, int))

        abstract_meal = AbstractMeal(name=name, price=price)

        self.assertEqual(abstract_meal.name, name)
        self.assertEqual(abstract_meal.price, price)


if __name__ == '__main__':
    unittest.main()
