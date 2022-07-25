from abc import ABC, abstractmethod

class LightCommand(ABC):
   @abstractmethod
   def execute(self): pass
   
   @abstractmethod
   def undo(self): pass
   