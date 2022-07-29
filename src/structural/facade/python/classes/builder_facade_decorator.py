from classes.facade.builder_facade import BuilderFacade


class BuilderFacadeDecorator():
    def __init__(self):
        self.facade = BuilderFacade()

    def before(self):
        self.facade.main_dish_builder.reset()
        self.facade.vegan_dish_builder.reset()

    def make_meal_with_two_builder(self):
        self.before()
        self.facade.make_meal_with_two_builder()
        print('\n >> Finish make_meal_with_two_builder\n')

    def make_meal_without_builder(self):
        self.before()
        self.facade.make_meal_without_builder()
        print('\n >> Finish make_meal_without_builder\n')
