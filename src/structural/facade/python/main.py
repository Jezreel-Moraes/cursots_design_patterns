# I used the builder pattern to create a facade to not have to create a
# new complex code...

# I used an decorator to reset the internal
# objects in builderFacade before each new method call...

from classes.builder_facade_decorator import BuilderFacadeDecorator

builderFacade = BuilderFacadeDecorator()
builderFacade.make_meal_with_two_builder()
builderFacade.make_meal_without_builder()
