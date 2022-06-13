from image_editor import *

def no_using_backup():
   print('No backup:')
   image_editor = ImageEditor('/media/image.png', 'png')
   print(image_editor)
   
   image_editor.convert_format_to('jpg')
   print(image_editor)



def using_backup():
   print('Using backup:')
   image_editor = ImageEditor('/media/image.png', 'png')
   print(image_editor)

   backup_manager = ImageEditorBackupManager(image_editor)
   backup_manager.backup()
   
   image_editor.convert_format_to('jpg')
   print(image_editor)
   
   backup_manager.restore()
   print(image_editor)


if __name__ == '__main__':
   no_using_backup()
   print('\n')
   using_backup()
   
   
