import abc


class MealCompositeProtocol(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def get_price(self) -> int: pass
