if __package__ is None or __package__ == '':
   # print(f'no package - init Interfaces')
   from meal_composite_protocol import MealCompositeProtocol
   from meal_builder_protocol import MealBuilderProtocol
else:
   # print(f'package : {__package__} - init Interfaces')
   from .meal_composite_protocol import MealCompositeProtocol
   from .meal_builder_protocol import MealBuilderProtocol


if __name__ == "__main__":
   print('init meal')