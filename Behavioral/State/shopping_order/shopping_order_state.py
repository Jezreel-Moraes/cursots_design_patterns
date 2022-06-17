from abc import ABC, abstractmethod


class ShoppingOrderState(ABC):
   
   @abstractmethod
   def get_name(self) -> str: pass
   
   @abstractmethod
   def approve_payment(self) -> None: pass
   
   @abstractmethod
   def reject_payment(self) -> None: pass
   
   @abstractmethod
   def wait_payment(self) -> None: pass
   
   @abstractmethod
   def ship_order(self) -> None: pass