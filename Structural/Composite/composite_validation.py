from abc import ABCMeta, abstractclassmethod
from typing import Any, List, Tuple
from functools import reduce

#interface
class ValidationComponent(metaclass=ABCMeta):
   @abstractclassmethod
   def validate(self, value: Any) -> bool: pass
   
   def add(component: type) -> None: pass

#leaf
class ValidateEmail(ValidationComponent):
   def validate(self, value: Any) -> bool: 
      if isinstance(value, str): return '@' in value
   
#leaf
#leaf
class ValidateString(ValidationComponent):
   def validate(self, value: Any) -> bool: 
      return isinstance(value, str)
   
#leaf
class ValidateInt(ValidationComponent):
   def validate(self, value: Any) -> bool: 
      return isinstance(value, int)

#composite
class ValidateCompositor(ValidationComponent):
   def __init__(self) -> None:
      self.children : List[ValidationComponent] = []
   
   def add(self, *args: List[ValidationComponent] | Tuple[ValidationComponent]):
      for item in args: self.children.append(item)
   
   def validate(self, value: Any) -> bool: 
      for validator in self.children:
         if not validator.validate(value): 
            print(validator.__class__.__name__)
            return False
      return True
   
if __name__ == '__main__':
   e = ValidateEmail()      
   i = ValidateInt()      
   s = ValidateString()      

   c = ValidateCompositor()
   c.add(e, i, s)
   
   print( c.validate(1))
   

   
