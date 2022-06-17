from typing import Protocol
from product_protocol import VisitableProductProtocol


class TaxVisitor(Protocol):
   @staticmethod
   def calculate_taxes_for_vehicle(o: VisitableProductProtocol) -> float:
      pass
   
   @staticmethod
   def calculate_taxes_for_food(o: VisitableProductProtocol) -> float:
      pass
   
   @staticmethod
   def calculate_taxes_for_medicine(o: VisitableProductProtocol) -> float:
      pass
   
   