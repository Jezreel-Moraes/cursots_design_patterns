# I used the builder pattern to create a facade because of its complexity,
# to not have to create a new complex code... 

# I used an decorator pattern too because i have to reset the internal 
# objects in the facade in each new method call...

from builder_facade import BuilderFacadeDecorator

builderFacade = BuilderFacadeDecorator()
builderFacade.make_meal_with_two_builder()
builderFacade.make_meal_with_builder_2()
builderFacade.make_meal_with_builder_1()
builderFacade.make_meal_without_builder()
builderFacade.make_meal_build_without_list()
