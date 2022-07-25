from .memento import Memento

class ConcreteMemento(Memento):
   def __init__(
         self, 
         name: str,
         date: str,
         file_path: str,
         file_format: str
      ) -> None:
      
      self.name = name
      self.date = date
      self.file_path = file_path
      self.file_format = file_format
   
   
   def get_name(self) -> str: 
      return self.name
   
   def get_date(self) -> str: 
      return self.date
   
   def get_file_path(self) -> str:
      return self.file_path
   
   def get_file_format(self) -> str:
      return self.file_format