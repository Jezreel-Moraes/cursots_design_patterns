from typing import Union
from dataclasses import dataclass, field
from iterator_protocol import Iterator


@dataclass
class DataStructure:
   items: Union[str, int]
   iterator: Iterator | None = None
   
   def add_item(self, *items: Union[str,int] | Union[str, int] | str | int) -> None:
      if isinstance(items, list) or isinstance(items, tuple):
         self.items.extend(items)
      else:
         self.items.append(items)
   
   def get_items(self) -> Union[str, int]:
      return self.items
   
   def size(self) -> int:
      return len(self.items)
   
   def set_iterator(self, iterator: Iterator) -> None:
      self.iterator = iterator
      
   def __iter__(self) -> Iterator:
      return self.iterator
   
   def reset_iterator(self) -> None:
      self.iterator.reset()