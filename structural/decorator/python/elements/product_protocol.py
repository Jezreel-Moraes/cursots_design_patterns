from abc import ABCMeta, abstractclassmethod

class ProductProtocol(metaclass=ABCMeta):
    @abstractclassmethod
    def get_price(self) -> int: pass
    @abstractclassmethod
    def get_name(self) -> str: pass