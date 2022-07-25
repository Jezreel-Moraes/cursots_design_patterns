from .memento import Memento
from .image_editor import ImageEditor
from typing import List

class ImageEditorBackupManager:
   def __init__(self, image_editor: ImageEditor) -> None:
      self.mementos: List[Memento] = []
      self.image_editor = image_editor
        
   def backup(self) -> None:
      print('Backup: Saving the current state of the image editor!')
      self.mementos.append(self.image_editor.save())
      
   def restore(self) -> None:
      
      memento = self.mementos.pop()
      if (not memento):
         print('Backup: No mementos!')
         return
      
      self.image_editor.restore(memento)
      print(f'Backup: {memento.get_name()} has successfully been restored.')
      