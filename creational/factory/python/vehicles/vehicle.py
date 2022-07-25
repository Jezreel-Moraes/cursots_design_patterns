import abc

class Vehicle(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def pick_up(self, customer_name: str) -> None: pass
   @abc.abstractmethod
   def stop(self) -> None: pass
   
   def __repr__(self) -> str:
      return str(self.__dict__)
      