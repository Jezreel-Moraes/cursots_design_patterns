from typing import Tuple
from observer_protocol import *


class SoccerTeam(Subject):

   def __init__(self, team_name: str) -> None:
      super().__init__()
      self.team_name = team_name

   def subscribe(self, *observers: Tuple[Observer] | Observer) -> None: 
      
      if isinstance(observers, Observer): 
         observers = (observers)
         
      for observer in observers:
         if observer in self.observers: continue
         self.observers.append(observer)

   def unsubscribe(self, observer: Observer) -> None: 
      if observer in self.observers:
         self.observers.remove(observer)      

   def notify(self, type: str, scored: bool) -> None: 
      command = {
         'type': type,
         'scored': scored    
      }
      
      for observer in self.observers:
         observer.update(command)
         
   def score_goal(self) -> None: 
      print(f'{self.team_name} scored a goal!')
      self.notify(type='goal', scored=True)
      
   def concede_goal(self) -> None: 
      print(f'{self.team_name} conceded a goal!')
      self.notify(type='goal', scored=False)
