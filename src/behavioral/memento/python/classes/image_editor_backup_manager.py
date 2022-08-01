from classes.image_editor import ImageEditor
from classes.interfaces.memento import Memento


class ImageEditorBackupManager:
    def __init__(self, image_editor: ImageEditor) -> None:
        self.mementos: list[Memento] = []
        self.image_editor = image_editor

    def backup(self) -> None:
        print('Backup: Saving the current state of the image editor!')
        self.mementos.append(self.image_editor.save())

    def restore(self) -> None:

        try:
            memento = self.mementos.pop()
        except IndexError as error:
            error = error
            print('Backup: No mementos!')
            return

        self.image_editor.restore(memento)
        print(f'Backup: {memento.get_name()} has successfully been restored.')
