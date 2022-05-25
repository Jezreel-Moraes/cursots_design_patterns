import abc

class MealCompositeProtocol(metaclass=abc.ABCMeta):
   @abc.abstractclassmethod
   def get_price(self) -> int: return

if __name__ == "__main__" : print('meal')