from abc import ABCMeta, abstractclassmethod

class ValidationsInterface(metaclass=ABCMeta):
   @abstractclassmethod
   def is_email(email: str) -> bool: pass
   def is_email(email: str) -> bool: pass