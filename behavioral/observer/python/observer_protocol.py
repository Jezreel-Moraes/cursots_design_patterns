from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
   
   @abstractmethod
   def update(self, command) -> None:
      pass


class Subject(ABC):
   def __init__(self) -> None:
      self.observers: List[Observer] = []
      
   @abstractmethod
   def subscribe(self, observer: Observer) -> None: 
      pass
   
   @abstractmethod
   def unsubscribe(self, observer: Observer) -> None: 
      pass
   
   @abstractmethod
   def notify(self) -> None: 
      pass
   
   