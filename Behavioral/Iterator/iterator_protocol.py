from typing import Protocol


class Iterator(Protocol):
   def __init__(self) -> None:
      self.index: int
      self.last: int
      
   def __iter__(self) -> "Iterator":
      ...
      
   def __next__(self) -> None:
      ...   
      
   def has_next(self) -> bool:
      ...
      
   def reset(self) -> None:
      ...         
      