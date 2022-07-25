from data_structure import DataStructure


class IteratorForward:
   def __init__(self, data_structure: DataStructure) -> None:
      self.data_structure: DataStructure = data_structure
      self.index: int = 0
      self.last: int = data_structure.size()
      
   def reset(self) -> None:
      self.index = 0
      
   def __iter__(self) -> "IteratorForward":
      return self   
   
   def __next__(self) -> str | int:
      if not self.has_next():
         raise StopIteration
      
      item: str | int = self.data_structure.items[self.index]
      self.index += 1
      return item
      
   def has_next(self) -> bool:
      return self.index < self.last