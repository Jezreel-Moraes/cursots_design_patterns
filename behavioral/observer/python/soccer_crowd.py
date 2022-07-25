from observer_protocol import *


class SupporterTeam(Observer):
   def __init__(self) -> None:
      self.accepted_commands = {
         'goal': lambda command: self.check_goal(command),
      }
   
   def check_goal(self, command) -> None:
      self.celebrate() if command['scored'] else self.cry()
      
   def celebrate(self) -> None:   
      print('\tSupporter Team is celebrating!')
   
   def cry(self) -> None:
      print('\tSupporter Team is crying!')
   
   def update(self, command) -> None:
      update_function = self.accepted_commands[command['type']]
      if update_function is None or not callable(update_function): return
      update_function(command)
      
      
class AdversarySupporterTeam(Observer):
   def __init__(self) -> None:
      self.accepted_commands = {
         'goal': lambda command: self.check_goal(command),
      }
   
   def check_goal(self, command) -> None:
      self.cry() if command['scored'] else self.celebrate()
      
   def celebrate(self) -> None:   
      print('\tAdversary Supporter Team is celebrating!')
   
   def cry(self) -> None:
      print('\tAdversary Supporter Team is crying!')
   
   def update(self, command) -> None:
      update_function = self.accepted_commands[command['type']]
      if update_function is None or not callable(update_function): return
      update_function(command)