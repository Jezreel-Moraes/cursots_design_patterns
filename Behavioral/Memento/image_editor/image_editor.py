from datetime import datetime
from .memento import Memento
from .concrete_memento import ConcreteMemento

class ImageEditor:
   def __init__(self, file_path: str, file_format: str) -> None:
      self.file_path = file_path
      self.file_format = file_format
      
   def convert_format_to(self, format: str) -> None:
      self.file_format = format
      self.file_path = '.'.join([self.file_path.split('.')[0], self.file_format])
   
   def save(self) -> Memento:
      date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
      return ConcreteMemento(
         date,
         date,
         self.file_path,
         self.file_format
      )
      
   def restore(self, memento: ConcreteMemento) -> None:
      self.file_path = memento.get_file_path()
      self.file_format = memento.get_file_format()
      
   def __repr__(self) -> str:
      return str(f'{self.__class__.__name__} {{ file_path: {self.file_path}, file_format: {self.file_format} }}')