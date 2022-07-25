from abc import ABCMeta, abstractclassmethod
from typing import List, Tuple
from functools import reduce


class Component(metaclass=ABCMeta):
   @abstractclassmethod
   def get_price(self) -> int: pass
   
   def add(component: type) -> None: pass
   
class Leaf(Component):
   def __init__(self, name: str, price: int) -> None:
      self.name: str = name
      self.price: int = price
   
   def get_price(self) -> int: return self.price
   
class Compositor(Component):
   def __init__(self) -> None:
      self.children : List[Component] = []
   
   def add(self, *args: List[Component] | Tuple[Component]):
      for item in args: self.children.append(item)
   
   def get_price(self) -> int: 
      return reduce(lambda sum, component: sum + component.get_price() , self.children, 0)
   
if __name__ == '__main__':
   
   l1 = Leaf('l1', 12)   
   l2 = Leaf('l2', 125)   
   l3 = Leaf('l3', 1626)   

   c1 = Compositor()
   c1.add(l1, l2, l3)
   
   c2 = Compositor()
   c2.add(l3, l2, c1)
   
   c3 = Compositor()
   c3.add(c2, l2, c1)

   
