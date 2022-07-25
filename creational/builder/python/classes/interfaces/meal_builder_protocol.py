import abc

class MealBuilderProtocol(metaclass=abc.ABCMeta):
   @abc.abstractclassmethod
   def make_meal(self) -> type: pass

   # @abc.abstractclassmethod
   # def make_beverage(self) -> type: pass
   
   # @abc.abstractclassmethod
   # def make_dessert(self) -> type: pass
